from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional, List

from app.models.GeoCoordinate import GeoCoordinate
from app.models.responseobjects.externalapiresponse.WeatherApiBulkResponse import Hour


class WeatherRoutePoint:
    def __init__(self, Coordinates: GeoCoordinate, DistanceFromLastPoint: float,
                 DurationFromLastPoint: float, WeatherForecastAtDuration: Optional[Hour],
                 CompleteForecast: Optional[List[Hour]], lastpoint: Optional['WeatherRoutePoint']):

        self.DistanceFromLastPoint = DistanceFromLastPoint
        self.Coordinates = Coordinates
        self.DurationFromLastPoint = DurationFromLastPoint
        self.WeatherForecastAtDuration = WeatherForecastAtDuration
        self.CompleteForecast = CompleteForecast
        
        if lastpoint is not None:
            self.TotalDistance = DistanceFromLastPoint + lastpoint.TotalDistance
            self.TotalDuration = DurationFromLastPoint + lastpoint.TotalDuration
        else:
            self.TotalDistance = 0.0
            self.TotalDuration = 0.0
            

    def GetDinstanceTo(self, other: 'WeatherRoutePoint'):
        return self.Coordinates.GetDistanceTo(other.Coordinates)

    def FillHour(self, weatherForeCast: List[Hour], routeStartDate: Optional[datetime] = datetime.now()) -> None:
        
        dateTimeAtDuration = routeStartDate + timedelta(seconds=self.TotalDuration)

        weatherAtDuration = list(
            filter(lambda x: x.time.hour == dateTimeAtDuration.hour, weatherForeCast))[0]

        self.WeatherForecastAtDuration = weatherAtDuration
        self.CompleteForecast = weatherForeCast
