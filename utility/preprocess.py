import tensorflow as tf
import cv2
import numpy as np

def preprocess(image_file: bytes):
    # Load the image directly from bytes
    img = tf.io.decode_jpeg(image_file)
    # Preprocessing steps - resizing the image to be 100x100x3
    img = tf.image.resize(img, (100, 100))
    # Scale image to be between 0 and 1
    img = img / 255.0
    # Return image
    return img

def preprocessLive(image_file: bytes):

    image = cv2.imdecode(np.frombuffer(image_file, np.uint8), cv2.IMREAD_COLOR)

    image = cv2.resize(image, (150, 150))
    # Normalize the image
    image = image / 255.0
    # Reshape the image to add a batch dimension
    image = image.reshape(1, 150, 150, 3)
    return image