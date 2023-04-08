
import json
from flask import request, jsonify, Blueprint
from datetime import datetime

from app.models.requestobjects.RouteRequestObject import RouteRequestObject
from app.models.responseobjects.WeatherRouteResponse import WeatherRouteResponse
from app.services.RouteServices import GetWeatherRouteResponseObject

weatherController = Blueprint('weatherController', __name__)


@weatherController.route("/v1/WeatherRoute/GetWeatherRoute", methods=["POST"])
def getWeatherRoute():
    body = request.json

    if 'StartTime' not in body:
        body['StartTime'] = datetime.now()
    
    parsedBody: RouteRequestObject = RouteRequestObject.from_dict(body)

    responseObject = GetWeatherRouteResponseObject(parsedBody.CoordinatesStart, parsedBody.CoordinatesDestination, parsedBody.StartTime)

    json_string = json.dumps(responseObject, default=serialize_weather_route_response)
    return jsonify(responseObject)


def serialize_weather_route_response(obj):
    if isinstance(obj, WeatherRouteResponse):
        return {
            'coordinates_start': obj.coordinates_start.__dict__,
            'coordinates_destination': obj.coordinates_destination.__dict__,
            'start_time': obj.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            'finish_time': obj.finish_time.strftime('%Y-%m-%d %H:%M:%S'),
            'weather_route_points': obj.weather_route_points,
            'poly_line': obj.poly_line
        }
    return None