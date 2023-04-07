from datetime import datetime
from typing import Any
from dataclasses import dataclass
import json

@dataclass
class GeoCoordinateSimple:
    Latitude: float
    Longitude: float

    @staticmethod
    def from_dict(obj: Any) -> 'GeoCoordinateSimple':
        _Latitude = float(obj.get("Latitude"))
        _Longitude = float(obj.get("Longitude"))
        return GeoCoordinateSimple(_Latitude, _Longitude)


@dataclass
class RouteRequestObject:
    CoordinatesStart: GeoCoordinateSimple
    CoordinatesDestination: GeoCoordinateSimple
    StartTime: datetime

    @staticmethod
    def from_dict(obj: Any) -> 'RouteRequestObject':
        _CoordinatesStart = GeoCoordinateSimple.from_dict(obj.get("CoordinatesStart"))
        _CoordinatesDestination = GeoCoordinateSimple.from_dict(obj.get("CoordinatesDestination"))
        _StartTime = datetime.fromisoformat(obj.get("StartTime"))
        return RouteRequestObject(_CoordinatesStart, _CoordinatesDestination, _StartTime)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)