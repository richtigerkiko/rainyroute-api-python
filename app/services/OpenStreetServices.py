
import json
import requests

from app.models.GeoCoordinate import GeoCoordinate
from app.models.responseobjects.externalapiresponse.ORSMApiResult import ORSMApiResult


def GetOSRMApiResult (start:GeoCoordinate, destination:GeoCoordinate) -> ORSMApiResult:
    
    # Setup route Request
    url = f"http://router.project-osrm.org/route/v1/driving/{start.Longitude},{start.Latitude};{destination.Longitude},{destination.Latitude}"
    params = {
        "annotations": "true",
        "steps": "false",
        "overview": "full"
    }
    
    response = requests.get(url, params)
        
    parsedResponse = ORSMApiResult.from_dict(response.json())
    
    return parsedResponse
