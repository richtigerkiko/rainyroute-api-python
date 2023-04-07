
import json
from flask import request, jsonify, Blueprint
from datetime import datetime

from app.models.requestobjects.RouteRequestObject import RouteRequestObject
from app.services.RouteServices import GetWeatherRouteResponseObject

weatherController = Blueprint('weatherController', __name__)


@weatherController.route("/v1/WeatherRoute/GetWeatherRoute", methods=["POST"])
def getWeatherRoute():
    body = request.json

    if 'StartTime' not in body:
        body['StartTime'] = datetime.now()
    
    parsedBody: RouteRequestObject = RouteRequestObject.from_dict(body)

    responseObject = GetWeatherRouteResponseObject(parsedBody.CoordinatesStart, parsedBody.CoordinatesDestination, parsedBody.StartTime)

    
    return "ok"
