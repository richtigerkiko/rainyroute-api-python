from datetime import date, datetime
from flask.json.provider import DefaultJSONProvider
from flask import Flask
from flask_restful import Api

from app.controllers.weatherroute import weatherController


class CustomJsonEncoder(DefaultJSONProvider):
    def default(self, o):
        if isinstance(o, date) or isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)


def create_app():
    app = Flask(__name__)

    # register routes
    app.register_blueprint(weatherController)

    app.json = CustomJsonEncoder(app)
    
    app.config.from_prefixed_env()
    
    return app
