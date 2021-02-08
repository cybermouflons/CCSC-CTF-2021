import tensorflow
import numpy
import io
import os

from base64 import b64decode
from skimage import transform
from skimage.io import imread
from skimage.util.shape import view_as_blocks

DIM = 8                                                         # Chess board 8 x 8
SQUARE_SIZE = 40                                                # Tile size
PIECE_SYMBOLS = "prbnkqPRBNKQ "                                 # Chess piece symbols
LABEL2SYMBOL = {p:i for i, p in enumerate(PIECE_SYMBOLS)}       # Map to convert lables back to piece symbols
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

def preprocess_image(img: numpy.ndarray) -> numpy.ndarray:
    """Preprocess an image for using it as model input. Initially the image is downsampled
    and then it is split to blocks.

    Args:
        img (numpy.ndarray): Image as a numpy array

    Returns:
        numpy.ndarray: Preprocessed image 
    """
    downsample_size = SQUARE_SIZE*DIM

    img_read = transform.resize(
        img,
        (downsample_size, downsample_size),
        mode='constant'
    )[:,:,:3] # Drop alpha in case of png

    tiles = view_as_blocks(img_read, block_shape=(SQUARE_SIZE, SQUARE_SIZE, 3)).squeeze(axis=2)
    return tiles.reshape(DIM*DIM, SQUARE_SIZE, SQUARE_SIZE, 3)

def deserialize_image(img_payload: str) -> numpy.ndarray:
    """Returns an image byte-like object from base64 payload

    Args:
        img_payload (str): base64 encoded image

    Returns:
        bytes: Image as numpy array
    """
    return imread(io.BytesIO(b64decode(img_payload))) / 255

def reconstruct_from_blocks(img: numpy.ndarray) -> numpy.ndarray:
    """Reconstructs the original image from a given preprocessed image.
    The preprocessed image is split into blocks and this function stitches them back together.

    Args:
        preprocessed_img (numpy.ndarray): Preprocessed image as numpy array

    Returns:
        numpy.ndarray: Reconstructed image as numpy array
    """
    return img.numpy().reshape(
        DIM, DIM, SQUARE_SIZE, SQUARE_SIZE, 3
    ).transpose(0, 2, 1, 3, 4).reshape(
        SQUARE_SIZE * DIM,SQUARE_SIZE * DIM, 3
    )

def labels2fen(labels: numpy.ndarray) -> str:
    """Converts arithmetic piece symbol labels to fen notation

    Args:
        labels (numpy.ndarray): 

    Returns:
        str: FEN notation of the give piece labels
    """
    fen = "/".join("".join(PIECE_SYMBOLS[p] for p in row) for row in labels)
    for i in range(DIM, 0, -1):
       fen = fen.replace(' ' * i, str(i))
    return fen

def fen2labels(fen: str) ->numpy.ndarray:
    """Converts fen notation to arithmetic labels. 

    Args:
        fen (str): FEN notation as string sequence

    Returns:
        numpy.ndarray: Numpy array containing the piece labels 
    """
    labels = []
    for row in fen.split("/"):
        row_labels = []
        for p in row:
            row_labels += (int(p) * [LABEL2SYMBOL[' ']] if p.isnumeric() else [LABEL2SYMBOL[p]])
        labels += [row_labels]
    return numpy.array(labels)

def difference(img_a: numpy.ndarray, img_b: numpy.ndarray) -> numpy.float64:
    """Returns the maximum difference amongst the pixels of two images.

    Args:
        img_a (numpy.ndarray): Image A as numpy array
        img_b (numpy.ndarray): Image B as numpy array

    Returns:
        numpy.float64: Pixel difference
    """
    difference = (img_a - img_b).reshape(-1)
    return max(difference.max(), abs(difference.min()))

def is_visually_similar(img_a: numpy.ndarray, img_b: numpy.ndarray, threshold: float) -> bool:
    """Checks whether two images are visually similar given  difference threshold.
    The lower the threshold, the more visually similar the images must be

    Args:
        img_a (numpy.ndarray): Image A as numpy array
        img_b (numpy.ndarray): Image B as numpy array
        threshold (float): Difference threshold

    Returns:
        bool: True if similarity is below threshold, False otherwise
    """
    diff = difference(img_a, img_b)
    print("diff: ", diff)
    return diff <= threshold 

def predict_fen(img: numpy.ndarray, model_path: str = os.path.join(BASE_DIR,"model")) -> str:
    """Predicts the FEN notation of the given board image.
    Image dimensions must be 320x320

    Args:
        img (numpy.ndarray): Image as numpy array
        model_path (str): Path of the saved model to use
        
    Returns:
        str: FEN notation as a string 
    """
    model = tensorflow.keras.models.load_model(model_path)
    prediction = model.predict(img)
    board = prediction.argmax(axis=1).reshape(DIM, DIM)
    return labels2fen(board)