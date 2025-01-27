import numpy as np
import base64
from io import BytesIO
from PIL import Image
import requests
import json
from tensorflow.keras.applications.densenet import DenseNet121, preprocess_input, decode_predictions
from fastapi import FastAPI, HTTPException, File, UploadFile, Request
from fastapi.responses import JSONResponse


def preprocess_image(image: Image.Image):
    
    """Preprocess the image for DenseNet121."""
    input_size = (224, 224)  # Model expects 224x224 input
    image = image.resize(input_size)  
    image = image.convert("RGB")
    image_array = np.array(image)  
    image_array = preprocess_input(image_array)  
    image_array = np.expand_dims(image_array, axis=0)
    return image_array


model = DenseNet121(weights=None)
model.load_weights('./pre_trained_model/densenet121_weights_tf_dim_ordering_tf_kernels.h5')


# Initializing FastAPI app
app = FastAPI()
        

# Defining the post method for predictions
# The method accepts either an image file or
# a json payload of the form {'image'='img_data'}
@app.post("/predict/")
async def predict(request : Request, image: UploadFile = File(None)):
    try:
        if image:
            image_content = await image.read()

            image = Image.open(BytesIO(image_content))

        else:
            try:
                request_data = await request.json()

                encoded_image = request_data['image']

                binary_image = base64.b64decode(encoded_image)

                image = Image.open(BytesIO(binary_image))

            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Invalid JSON payload: {str(e)}")
        

        processed_image = preprocess_image(image)

        # Make predictions
        predictions = model.predict(processed_image)
        top_prediction = decode_predictions(predictions, top=1)[0][0]

        predicted_class = str(top_prediction[1])

        return JSONResponse(content={"response": predicted_class})

    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the image: {str(e)}")

# Root
@app.get("/")
def root():
    return {"message": "Welcome to the Image Classification API!"}


### To launch the server use the bash command

# uvicorn python_scripts.Loading_model:app --host 0.0.0.0 --port 8000