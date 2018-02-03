#New -- it works


import io
import os

import PIL
from PIL import Image, ImageDraw, ImageFont

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

name = 'hi.jpg'

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    name)

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

x = 0

for label in labels:
    if (x == 0):
        x = x + 1
        y = label.description
        # print(y)

image = Image.open(name)
# font_type = ImageFont.truetype('Arial.tff', 20)                     // if you want to change the font
draw = ImageDraw.Draw(image)
draw.text(xy=(100, 50), text = y, fill=(255, 69, 0))
image.show()


