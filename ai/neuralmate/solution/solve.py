import tensorflow
import numpy
import os
import sys
import chess

from base64 import b64encode
from skimage.io import imread, imsave
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from pwn import *

sys.path.append("../public/")

from neuralmate import preprocess_image, fen2labels, reconstruct_from_blocks, predict_fen

HOST = "localhost"
PORT = 4000
MODEL_PATH = "../public/model"
BOARDS_PATH = "../public/boards"

EPS = 20/255
STEPS = 150


def clip_eps(tensor, eps):
	return tensorflow.round(tensorflow.clip_by_value(tensor, clip_value_min=-eps, clip_value_max=eps))


def serialize_image(img_path):
    with open(img_path, "rb") as f:
        return b64encode(f.read())


def generate_adversarial_perturbation(model, img_base, delta, base_pred, target_pred, eps, optimizer, steps):
    
    for step in range(steps):
        with tensorflow.GradientTape() as tape:
            
            tape.watch(delta)

            adversarial_example = img_base + delta

            prediction = model(adversarial_example, training=False)

            base_pred_labels = fen2labels(base_pred)
            target_pred_labels = fen2labels(target_pred)

            loss = SparseCategoricalCrossentropy(from_logits=True, reduction="auto")
            original_loss = -loss(tensorflow.convert_to_tensor(base_pred_labels), prediction)
            target_loss = loss(tensorflow.convert_to_tensor(target_pred_labels), prediction)

            total_loss = target_loss + original_loss

            if step % 10 == 0:
                print("step: {}, loss: {}...".format(step, total_loss.numpy()))
            
        gradients = tape.gradient(total_loss, delta)

        optimizer.apply_gradients([(gradients, delta)])
        delta.assign_add(clip_eps(delta, eps=eps))
    
    return delta

if __name__ == "__main__":
    io = remote("localhost", 4000)
    
    groundtruth_boards = [
        ("Diagonally correct", "board1.png", "r4rk1/ppp2ppp/8/8/8/1P6/PQ3PPP/R4RK1", "r4rk1/ppp2ppp/8/8/8/1P6/PQ3PPP/B4RK1", "b2g7"),
        ("Couldn't be smothered", "board2.png", "r5rk/ppp3pp/8/4P3/8/1P6/P4PPP/5RK1", "r5rk/ppp3pp/8/4N3/8/1P6/P4PPP/5RK1", "e5f7"),
        ("Two is always better than one", "board3.png", "7k/p6p/1p6/8/8/R7/B4K2/8", "7k/p6p/1p6/8/8/B7/B4K2/8", "a3b2"),
    ]

    model = tensorflow.keras.models.load_model(MODEL_PATH)
    optimizer = Adam(lr=0.5, beta_1=0.8, beta_2=0.999, epsilon=1e-08, decay=0.0)

    for board_name, board_file, original_fen, target_fen, mate_move in groundtruth_boards:

        print(io.recvuntil("Image: "))

        img = imread(os.path.join(BOARDS_PATH, board_file))
        img = preprocess_image(img)
        img_original = tensorflow.constant(img, dtype=tensorflow.float32)

        print("[+] Generating image perturbation...")

        delta = tensorflow.zeros_like(img_original)
        delta = tensorflow.Variable(
            delta, trainable=True, constraint=lambda x: tensorflow.clip_by_value(x, -.057, .057)
        ) 


        perturbation = generate_adversarial_perturbation(
            model,
            img_original,
            delta,
            original_fen,
            target_fen,
            eps=EPS,
            optimizer=optimizer,
            steps=STEPS
        )

        adv_blocks = img_original + perturbation

        adv_board_img = reconstruct_from_blocks(adv_blocks)
        adv_fen = predict_fen(adv_blocks, model_path=MODEL_PATH)

        print("Target:", target_fen)
        print("Adv:", adv_fen)

        assert adv_fen == target_fen

        board = chess.Board(adv_fen + " w")
        move = chess.Move.from_uci(mate_move)
        board.push(move)

        assert board.is_checkmate()

        adv_img_path = "adv_" + board_file
        adv_board_img = numpy.clip(adv_board_img, 0, 1)
        imsave(adv_img_path, adv_board_img)

        img_payload = b64encode(open(adv_img_path, "rb").read())
        
        io.sendline(img_payload)
        print(io.recvuntil("'a2a4'): "))
        io.sendline(mate_move)

    io.interactive()
        



        
