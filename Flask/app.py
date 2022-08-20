import os
from flask import Flask,render_template

# videoที่ถูกuploadบนเว็บจะถูกเก็บไว้ที่ folder saveVdo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, './static/saveVdo')


app = Flask(__name__, template_folder='template')
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024