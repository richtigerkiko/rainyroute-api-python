from flask import Flask
from flask_restful import Api

from app.controllers.weatherroute import weatherController

def create_app():
    app = Flask(__name__)
    # api = Api(app)
    
    
    # register routes
    app.register_blueprint(weatherController)
    
    
    return app