import numpy

from keras.applications import resnet50
from keras.preprocessing import image

size = 224

model = resnet50.ResNet50()

def dog_detector(data):
  prediction = numpy.argmax(data)
  return ((prediction <= 268) & (prediction >= 151))

def run_model(img_path):
  img = image.load_img(path=img_path, target_size=(size, size))
  img = image.img_to_array(img)
  img = numpy.expand_dims(img, axis=0)
  img = resnet50.preprocess_input(img)
  img_pred = model.predict(img)

  if dog_detector(img_pred):
    return display_prediction(resnet50.decode_predictions(img_pred, top=1))
  else:
    return False


def display_prediction(pred_class):
  return pred_class[0].name
