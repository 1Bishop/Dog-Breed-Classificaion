import numpy

from keras.applications import resnet50
from keras.preprocessing import image


images_array = [
  "img/lab.jpg",
  "img/pug.jpg",
  "img/german.jpg",
  "img/hamster.jpg",
  "img/cat1.jpeg",
  "img/cat2.jpg",
  "img/elon1.jpg",
  "img/elon2.jpg"
]

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

  print("----------\n")
  if dog_detector(img_pred):
    print(img_path + " is a dog image and is: \n")
    display_prediction(resnet50.decode_predictions(img_pred, top=1))
    print("\n----------\n")
  else:
    print(img_path + " is not a dog photo!! \n")
    print("----------\n")

def display_prediction(pred_class):
  for imagenet_id, name, likelihood in pred_class[0]:
      print(" - {}: {:2f} likelihood".format(name, likelihood))


for img in images_array:
  run_model(img)
