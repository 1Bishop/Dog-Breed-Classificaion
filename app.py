from flask import Flask, request
app = Flask(__name__)

from PIL import Image
import numpy

from keras.applications import resnet50
from keras.preprocessing import image

size = 224, 224

model = resnet50.ResNet50()

def dog_detector(data):
  prediction = numpy.argmax(data)
  return ((prediction <= 268) & (prediction >= 151))


@app.route("/", methods=["POST"])
def home():
    img = Image.open(request.files['file'])

    img = img.load_img(img, target_size=(size, size))

    img = image.img_to_array(img)
    img = numpy.expand_dims(img, axis=0)
    img = resnet50.preprocess_input(img)
    img_pred = model.predict(img)

    if dog_detector(img_pred):
      return "success"
    else:
      return "not dog"

