# Good tutorial:
# http://www.angryobjects.com/2011/10/15/http-with-python-pycurl-by-example/

# How to use curl on terminal:
# curl -X POST \
#      -H "Content-Type: application/json" \
#      -d '{"name": "aa",
#           "address": "bb",
#           "business_type": "cc",
#           "coordinates": [100, 1],
#           "images": [],
#           "contributor": "dd"}' \
#      http://127.0.0.1:8000/dirban/1.0/business/

import base64
import json
import os
import os.path
import requests


# collection of pictures
PICS_FOLDER = 'pics'

# network setting
HOST = "127.0.0.1"
PORT = "8000"
RESOURCE = "/dirban/1.0/business/"
URL = "http://" + HOST + ":" + PORT + RESOURCE

# convert images in 'pics' folder to string in base64 format
images_base64 = []
for pic in os.listdir(PICS_FOLDER):
    image_path = os.path.join(PICS_FOLDER, pic)
    with open(image_path, 'rb') as image_file:
        images_base64.append(base64.b64encode(image_file.read()))

# set up header
headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}

# data that will be serialized in JSON format
data = {
    "name": "Warung Lela",
    "address": "Jalan Kupa No. 6, Cigadung, Bandung, Jawa Barat, 40135",
    "business_type": "Restaurant",
    "coordinates": [107.62784, -6.87253],
    "images": images_base64,
    "contributor": "winnuayi"
}

print json.dumps(data)
# send data
r = requests.post(URL, data=json.dumps(data), headers=headers)

print r.text
