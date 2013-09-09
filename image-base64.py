# TODO Write server which receive JSON data from json-sender.py

import base64
import cStringIO
import os.path
import PIL.Image


IMAGE_PATH = os.path.join('pics', 'wale1.jpg')

# encode
with open(IMAGE_PATH, 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read())

# decode
data = base64.b64decode(encoded_string)

# construct image buffer
file_like = cStringIO.StringIO(data)
img = PIL.Image.open(file_like)

# show
#img.show()

# write to image file
img.save('output_wale1.jpg')
