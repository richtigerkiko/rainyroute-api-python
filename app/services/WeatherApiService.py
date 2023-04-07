

from typing import List
import requests
from app.models.GeoCoordinate import GeoCoordinate

from app.models.WeatherRoutePoint import WeatherRoutePoint
from app.models.responseobjects.externalapiresponse.WeatherApiBulkResponse import WeatherApiBulkResponse


def AddWeatherToGeoWeatherList ( weatherpoints:List[WeatherRoutePoint] ) -> List[WeatherRoutePoint]:
    coordinateArray:List[GeoCoordinate] = []
    
    for point in weatherpoints:
        coordinateArray.append(point.Coordinates)
    
    weatherApiResult = GetWeatherApiBulkResponse(coordinateArray)
    
    
    for i, point in enumerate(weatherpoints):
        point.FillHour(next(filter(lambda x: x.query.custom_id == i, weatherApiResult.bulk), None))
    
    return weatherpoints
    
def GetWeatherApiBulkResponse (coordinates:List[GeoCoordinate]) -> WeatherApiBulkResponse:
    
    # Setup route Request
    url = f"http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": "true",
        "q": "bulk",
        "days": "1"
    }
    
    # Setup location request json for requestbody
    queryString = ""
    for i, coordinate in enumerate(coordinates):
        queryString += f"{{custom_id: '{i}', q: '{coordinate.Latitude}', '{coordinate.Longitude}'}},"
    
    requestBody = f"{{locations: [{queryString}]}}"
    
    
    response = requests.post(url=url, params=params, data=requestBody)
        
    parsedResponse = WeatherApiBulkResponse.from_dict(response.json())
    
    return parsedResponse
