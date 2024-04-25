import uvicorn
from fastapi import FastAPI, File, UploadFile
from routes.predict import predictSimilarity, predictLiveliness
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return "Model Server is Up!"

@app.post("/siamese/predict")
async def predict(image1: UploadFile = File(...), image2: UploadFile = File(...)):
    image1_data = await image1.read()
    image2_data = await image2.read()
    return predictSimilarity(image1_data, image2_data)

@app.post("/check-liveness")
async def check_liveness(image: UploadFile = File(...)):
    image_data = await image.read()
    return predictLiveliness(image_data)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)