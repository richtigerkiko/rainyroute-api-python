
from datetime import datetime
from typing import List
from app.models.GeoCoordinate import GeoCoordinate
from app.models.WeatherRoutePoint import WeatherRoutePoint
from app.models.responseobjects.WeatherRouteResponse import WeatherRouteResponse
from app.models.responseobjects.externalapiresponse.ORSMApiResult import Annotation
from app.services.OpenStreetServices import GetOSRMApiResult


def GetWeatherRouteResponseObject(start: GeoCoordinate, destination:GeoCoordinate, starttime: datetime) -> WeatherRouteResponse:
    osrmApiResult = GetOSRMApiResult(start, destination)
    
    # Simplify variables for better readability
    geometry = osrmApiResult.routes[0].geometry
    annotation = osrmApiResult.routes[0].legs[0].annotation
    
    weatherpoints = MergePolylineCoordinatesWithOSRMAnnotation(geometry, annotation)
    
    return None

def MergePolylineCoordinatesWithOSRMAnnotation (geometry: str, annotation: Annotation) -> List[WeatherRoutePoint]:
    pass