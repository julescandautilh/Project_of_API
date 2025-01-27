import base64
from PIL import Image
from io import BytesIO

path_image_to_encode = "./testing_data/example_boat.jpg"
path_encoded_small_image = "./testing_data/boat_image.txt"
path_decoded_small_image = "./testing_data/decoded_boat_image.jpg"

with open(path_image_to_encode, 'rb') as file:
    encoded_string = base64.b64encode(file.read())

with open(path_encoded_small_image, 'wb') as file:
    file.write(encoded_string)

with open(path_encoded_small_image, 'rb') as file:
    bytes_stream = base64.b64decode(file.read())
    io_bytes = BytesIO(bytes_stream)

with open(path_decoded_small_image, 'wb') as file:
    file.write(io_bytes.getvalue())
