from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional, List

from app.models.GeoCoordinate import GeoCoordinate
from app.models.responseobjects.externalapiresponse.WeatherApiBulkResponse import Hour


class WeatherRoutePoint:
    def __init__(self, DistanceFromLastPoint: float, Coordinates: GeoCoordinate,
                 TotalDuration: float, DurationFromLastPoint: float, WeatherForecastAtDuration: Optional[Hour],
                 CompleteForecast: Optional[List[Hour]], TotalDistance: Optional[float] = 0):
        self.TotalDistance = TotalDistance
        self.DistanceFromLastPoint = DistanceFromLastPoint
        self.Coordinates = Coordinates
        self.TotalDuration = TotalDuration
        self.DurationFromLastPoint = DurationFromLastPoint
        self.WeatherForecastAtDuration = WeatherForecastAtDuration
        self.CompleteForecast = CompleteForecast

    def GetDinstanceTo(self, other: 'WeatherRoutePoint'):
        return self.Coordinates.GetDistanceTo(other.Coordinates)
    
    def FillHour (self, weatherForeCast: List[Hour], routeStartDate:datetime) -> None:
        dateTimeAtDuration = routeStartDate + timedelta(seconds=self.TotalDuration)
        
        weatherAtDuration = list(filter(lambda x: x.time.hour == dateTimeAtDuration.hour, weatherForeCast))[0]
        
        self.WeatherForecastAtDuration = weatherAtDuration
        self.CompleteForecast = weatherForeCast
        