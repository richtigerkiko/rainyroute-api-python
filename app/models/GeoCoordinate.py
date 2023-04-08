from dataclasses import dataclass
import math
from typing import Optional

@dataclass
class GeoCoordinate:
    Latitude: float
    Longitude: float
    Altitude: Optional[float] = 0.0
    Speed: Optional[float] = 0.0
    Course: Optional[float] = 0.0
    

    # Calculates the distance between two geocoordinates. 
    # Because I'm bad at math i used google https://www.sunearthtools.com/tools/distance.php 
    # distance (A, B) = R * arccos (sin(latA) * sin(latB) + cos(latA) * cos(latB) * cos(lonA-lonB))
    def GetDistanceTo(self, other: 'GeoCoordinate'):
        earthRadiusInMeters= 6372.795477598 * 1000
        
        # simplfy function call for better readability
        tr = self.ToRadiants
        
        sinLatA = math.sin(tr(self.Latitude))
        sinLatB = math.sin(tr(other.Latitude))
        cosLatA = math.cos(tr(self.Latitude))
        cosLatB = math.cos(tr(other.Latitude))
        cosLonAMinusLonB = math.cos(tr(self.Longitude) - tr())
        
        distanceInMeters = earthRadiusInMeters * math.Acos(sinLatA * sinLatB + cosLatA * cosLatB * cosLonAMinusLonB)
        
        if other.Altitude != 0 & self.Altitude != 0:
            altitudeDifferenceMeters = other.Altitude - self.Altitude
            distanceInMeters = math.sqrt(distanceInMeters**2 - altitudeDifferenceMeters**2)
            
        return distanceInMeters
        
    
    def ToRadiants(deg: float):
        return deg * math.pi / 180
    