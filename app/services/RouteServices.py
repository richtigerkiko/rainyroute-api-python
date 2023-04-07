
from datetime import datetime, timedelta
from typing import List
import polyline
from app.models.GeoCoordinate import GeoCoordinate
from app.models.WeatherRoutePoint import WeatherRoutePoint
from app.models.responseobjects.WeatherRouteResponse import WeatherRouteResponse
from app.models.responseobjects.externalapiresponse.ORSMApiResult import Annotation
from app.services.OpenStreetServices import GetOSRMApiResult
from app.services.WeatherApiService import AddWeatherToGeoWeatherList


def GetWeatherRouteResponseObject(start: GeoCoordinate, destination: GeoCoordinate, starttime: datetime) -> WeatherRouteResponse:
    osrmApiResult = GetOSRMApiResult(start, destination)

    # Simplify variables for better readability
    geometry = osrmApiResult.routes[0].geometry
    annotation = osrmApiResult.routes[0].legs[0].annotation

    weatherpoints = MergePolylineCoordinatesWithOSRMAnnotation(geometry, annotation)

    weatherpoints = LowerAnnotationResolution(weatherpoints, 10000)

    weatherpoints = AddWeatherToGeoWeatherList(weatherpoints)

    returnObj = WeatherRouteResponse(start, 
                                     destination, 
                                     starttime, 
                                     (starttime + timedelta(seconds=osrmApiResult.routes[0].legs[0].duration) ), 
                                     weatherpoints,
                                     geometry
                                     )
    
    return returnObj


def MergePolylineCoordinatesWithOSRMAnnotation(geometry: str, annotation: Annotation) -> List[WeatherRoutePoint]:

    coordinateList = GetCoordinatesFromPolyline(geometry)

    returnObj: List[WeatherRoutePoint] = []

    # for (i = 0; i < coordinateList.Lengh; i++):
    for i in range(len(coordinateList)):
        distance = 0
        duration = 0
        coordinateList[i].Speed = 0

        lastObject = None

        if i != 0:
            coordinateList[i].Speed = annotation.speed[i - 1]
            distance = annotation.distance[i - 1]
            duration = annotation.duration[i - 1]
            lastObject = returnObj[-1]

        # course not implemented
        # if i < coordinateList.count() - 1:
        #     coordinateList[i].SetCourse(coordinateList[i-1])

        returnObj.append(WeatherRoutePoint(
            coordinateList[i], distance, duration, None, None, lastObject))

    return returnObj


def GetCoordinatesFromPolyline(polyLine: str) -> List[GeoCoordinate]:
    decoded = polyline.decode(polyLine)
    returnObj: List[GeoCoordinate] = []
    for obj in decoded:
        returnObj.append(GeoCoordinate(obj[0], obj[1]))
    return returnObj


def LowerAnnotationResolution(weatherPoints: List[WeatherRoutePoint], resolution: float):

    resultObj: List[GeoCoordinate] = []

    distanceCounter = 0.0
    durationCounter = 0.0

    for index, point in enumerate(weatherPoints):
        distanceCounter += point.DistanceFromLastPoint
        durationCounter += point.DurationFromLastPoint

        if (distanceCounter >= resolution) or (index == len(weatherPoints) -1) :
            point.DistanceFromLastPoint = distanceCounter
            point.DurationFromLastPoint = durationCounter

            resultObj.append(point)

            distanceCounter = 0.0
            durationCounter = 0.0

    return resultObj
