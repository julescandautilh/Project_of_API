### Welcome to the README of this API project!

## Introduction

# Please start by cloning the repo I sent you on your local machine


## Setting up the server (commands given in window cmd style)

# Create a virtual environment with python 3.12
# (tensorflow does not work on python 3.13)
# with the command:

conda create -n venv_name  python=3.12

# and activate it with

conda activate venv_name

# Then install the other requirments with pip:
 
pip install -r requirements.txt

# You can now launch the server using the bash command

uvicorn python_scripts.Loading_model:app --host 0.0.0.0 --port 8000

# This will turn the server on as well as load the pre-trained weights for the prediction ML model

# You can now send requests to the server
# either by directly sending a json object of the form

curl -X POST -H 'Content-type: application/json' -d '{\"image\": \"base64string\"}' http://127.0.0.1:8000/predict/

# or by giving the path of a locally saved image file (either 'jpg' or 'png')

curl -X POST -H "Content-Type: multipart/form-data" -F "@./path/to/file/example_image.png" http://127.0.0.1:8000/predict/

# Warning : if you are on windows and you get an Invoke-WebRequest error about parameter name -X, type

Remove-item alias:curl 

# before retrying the curl method


# Below are some examples

### Example curl request with base64 encoded image
curl -X POST -H 'Content-type: application/json' -d '{\"image\": \"iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAIAAADTED8xAAADMElEQVR4nOzVwQnAIBQFQYXff81RUkQCOyDj1YOPnbXWPmeTRef+/3O/OyBjzh3CD95BfqICMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMK0CMO0TAAD//2Anhf4QtqobAAAAAElFTkSuQmCC\"}' http://127.0.0.1:8000/predict/


### Example curl request that loads a locally stored image file
curl -X POST -H "Content-Type: multipart/form-data" -F "image=@./testing_data/example_dog.jpg" http://127.0.0.1:8000/predict/

# There are additional examples in the 'testing_data' folder

# I also left a python script called 'Encoding_decoding' to encode and decode additional images base64

# Finally, the python script 'Sending_data' allows a user to easily send json requests to the server:
# change the 'image_path' to your desired image and the script will detect if it's text file (and assume you send a base64 string)
# else, the script assumes that you are giving the path to the image (as .jpg or .png) to classify