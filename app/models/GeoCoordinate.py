from dataclasses import dataclass


@dataclass
class GeoCoordinate:
    Latitude: float
    Longitude: float
    Altitude: float
    Speed: float
    Course: float
    