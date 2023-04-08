

from typing import List
import requests
import json
from flask import current_app
from app.models.GeoCoordinate import GeoCoordinate

from app.models.WeatherRoutePoint import WeatherRoutePoint
from app.models.responseobjects.externalapiresponse.WeatherApiBulkResponse import WeatherApiBulkResponse


def AddWeatherToGeoWeatherList(weatherpoints: List[WeatherRoutePoint]) -> List[WeatherRoutePoint]:
    coordinateArray: List[GeoCoordinate] = []

    for point in weatherpoints:
        coordinateArray.append(point.Coordinates)

    weatherApiResult = GetWeatherApiBulkResponse(coordinateArray)

    for i, point in enumerate(weatherpoints):
        point.FillHour(
            next(filter(lambda x: x.query.custom_id == i, weatherApiResult.bulk), None).query.forecast.forecastday[0].hour)

    return weatherpoints


def GetWeatherApiBulkResponse(coordinates: List[GeoCoordinate]) -> WeatherApiBulkResponse:

    apiKey = current_app.config["RAINYROUTE_WEATHERAPIKEY"]

    # Setup route Request
    url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": apiKey,
        "q": "bulk",
        "days": "1"
    }

    # Setup location request json for requestbody
    queryString = ""

    requestBody = {
        'locations': [

        ]
    }
    
    for i, coordinate in enumerate(coordinates):
        requestBody["locations"].append({
            'custom_id': f'{i}', 
            'q': f"{coordinate.Latitude}, {coordinate.Longitude}"
        })
    
    


    response = requests.get(url=url, params=params,
                             json=requestBody)

    parsedResponse = WeatherApiBulkResponse.from_dict(response.json())

    return parsedResponse
