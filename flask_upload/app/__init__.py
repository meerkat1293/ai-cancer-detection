from flask import Flask

UPLOAD_FOLDER = 'C:\Users\meerm\OneDrive\Desktop\Uploads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

from app import routes