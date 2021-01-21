from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config.from_object(config_class)
    with app.app_context():
        from .import routes
        from .import forms
        from .import model
        from .import artifacts
        # from .artifacts import pipeline


    return app
