from flask import Flask
from .routes import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
