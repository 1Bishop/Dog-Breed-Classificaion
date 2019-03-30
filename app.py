import os
from flask import Flask, request, redirect
from werkzeug.utils import secure_filename
app = Flask(__name__)


UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from findDogForApi import *


@app.route("/", methods=["POST"])
def home():
  file = request.files['file']
  filename = secure_filename(file.filename)
  file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  img_path = "uploads/" + filename
  print(img_path)
  return run_model(img_path)



@app.route("/upload", methods=["POST"])
def upload():
  file = request.files['file']
  filename = secure_filename(file.filename)
  file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  # return redirect(url_for('uploaded_file', filename=filename))
  return filename
