from dataclasses import dataclass
from datetime import datetime
from typing import List

from app.models.GeoCoordinate import GeoCoordinate
from app.models.WeatherRoutePiont import WeatherRoutePoint


@dataclass
class WeatherRouteResponse:
    CoordinatesStart: GeoCoordinate
    CoordinatesDestination: GeoCoordinate
    StartTime: datetime
    FinishTime: datetime
    WeatherRoutePoints: List[WeatherRoutePoint]
    
