from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

# Test
from app import routes