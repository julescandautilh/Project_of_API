import requests
import base64
from PIL import Image
from io import BytesIO

# Define the server URL
url = "http://127.0.0.1:8000/predict/"

# Path to the local image file or base64 text file
image_path = "./testing_data/example_boat.jpg"

if image_path.endswith('.txt'):
    # Send the base64 as json payload
    with open(image_path, "r") as image_file:

            encoded_image = image_file.read()
            headers = {'Content-type': 'application/json'}
            payload = {"image": encoded_image}
            response = requests.post(url, headers=headers, json=payload)

else:
    # Send the image file as a File
    with open(image_path, "rb") as image_file:    
        response = requests.post(url, files={"image": image_file})

# Print the response from the server
print(response.json())
