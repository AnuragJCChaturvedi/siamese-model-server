import os
import tensorflow as tf

from utility.preprocess import preprocess, preprocessLive
from utility.customlayer import L1Dist
from tensorflow.keras.models import load_model
from fastapi.responses import JSONResponse

MPath = os.path.abspath('ai_models/siamesemodelv2.h5')
LMPath = os.path.abspath('ai_models/liveliness.h5')

def predictSimilarity(img1, img2):
    img1_array = preprocess(img1)
    img2_array = preprocess(img2)
    
    model = load_model(MPath, custom_objects={'L1Dist':L1Dist, 'BinaryCrossentropy':tf.losses.BinaryCrossentropy})
    predictions = model.predict([img1_array[None, :], img2_array[None, :]])  # Add batch dimension
    
    # Example assumes model output is a single accuracy value
    accuracy = predictions[0]

    return JSONResponse(content={"accuracy": float(accuracy)})

def predictLiveliness(img):
    img_array = preprocessLive(img)
    
    model = load_model(LMPath)
    predictions = model.predict(img_array)

    accuracy = predictions[0]
    return JSONResponse(content={"accuracy": float(accuracy)})