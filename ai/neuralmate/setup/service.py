import chess
import os

from skimage.io import imread
from neuralmate import preprocess_image, predict_fen, is_visually_similar, deserialize_image, BASE_DIR, difference
from secret import flag

welcome = """ __    _  _______  __   __  ______    _______  ___      __   __  _______  _______  _______ 
|  |  | ||       ||  | |  ||    _ |  |   _   ||   |    |  |_|  ||   _   ||       ||       |
|   |_| ||    ___||  | |  ||   | ||  |  |_|  ||   |    |       ||  |_|  ||_     _||    ___|
|       ||   |___ |  |_|  ||   |_||_ |       ||   |    |       ||       |  |   |  |   |___ 
|  _    ||    ___||       ||    __  ||       ||   |___ |       ||       |  |   |  |    ___|
| | |   ||   |___ |       ||   |  | ||   _   ||       || ||_|| ||   _   |  |   |  |   |___ 
|_|  |__||_______||_______||___|  |_||__| |__||_______||_|   |_||__| |__|  |___|  |_______|
by Benny Watts

Remember those boards I gave you...
Think you can beat me in ONE move?
Don't think so...

I don't even need to lift a finger, my neural network will take care of everything for me.
"""

if __name__ == "__main__":
    print(welcome)

    groundtruth_boards = [
        ("Diagonally correct", "board1.png"),
        ("Couldn't be smothered", "board2.png"),
        ("Two is always better than one", "board3.png"),
    ]

    try:
        for board_name, board_file in groundtruth_boards:
            serialized_img = input("Board '{0}' Image: ".format(board_name))
            board_img = deserialize_image(
                serialized_img
            )
            board_input = preprocess_image(board_img)
            fen = predict_fen(board_input).replace("-", "/")
            board = chess.Board(fen + " w") # The " w" postfix annotates that it's white's turn

            print("Board in FEN notation: {0}".format(fen))

            groundtruth_board_img = imread(os.path.join(BASE_DIR, "boards", board_file))
            groundtruth_board_img = preprocess_image(groundtruth_board_img)

            if not board.is_valid() or not is_visually_similar(
                groundtruth_board_img, board_input, 0.06
            ):
                raise ValueError("What is this? Are you serious?")

            move = input("What's your move (example: a2 to a4 would be 'a2a4'): ")
            move = chess.Move.from_uci(move)
            board.push(move)

            if not board.is_checkmate():
                raise ValueError("Not a checkmate for you buddy...")

            print("Can't be a check...mate... Let's go again!")

        print("It seems that I underestimated you... here is your flag: {0}".format(flag)) 

    except ValueError as e:
        message = e.args[0]
        print(message)

    except Exception as e:
        print(e)
        print("What the hell is that?")
