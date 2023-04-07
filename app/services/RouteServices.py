
from datetime import datetime
from app.models.GeoCoordinate import GeoCoordinate
from app.models.responseobjects.WeatherRouteResponse import WeatherRouteResponse
from app.services.OpenStreetServices import GetOSRMApiResult


def GetWeatherRouteResponseObject(start: GeoCoordinate, destination:GeoCoordinate, starttime: datetime) -> WeatherRouteResponse:
    osrmApiResult = GetOSRMApiResult(start, destination)
    
    
    
    return None