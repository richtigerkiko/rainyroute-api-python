
from flask import request, jsonify, Blueprint

weatherController = Blueprint('weatherController', __name__)


@weatherController.route("/v1/WeatherRoute/GetWeatherRoute", methods=["POST"])
def getWeatherRoute():
    content = request.json
    return "ok"