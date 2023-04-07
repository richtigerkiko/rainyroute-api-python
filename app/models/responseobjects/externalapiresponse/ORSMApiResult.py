from typing import List
from typing import Any
from dataclasses import dataclass


@dataclass
class Metadata:
    datasource_names: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'Metadata':
        _datasource_names = obj.get("datasource_names")
        return Metadata(_datasource_names)


@dataclass
class Annotation:
    metadata: Metadata
    datasources: List[int]
    weight: List[float]
    nodes: List[object]
    distance: List[float]
    duration: List[float]
    speed: List[float]

    @staticmethod
    def from_dict(obj: Any) -> 'Annotation':
        _metadata = Metadata.from_dict(obj.get("metadata"))
        _datasources = obj.get("datasources")
        _weight = obj.get("weight")
        _nodes = obj.get("nodes")
        _distance = obj.get("distance")
        _duration = obj.get("duration")
        _speed = obj.get("speed")
        return Annotation(_metadata, _datasources, _weight, _nodes, _distance, _duration, _speed)


@dataclass
class Leg:
    steps: List[object]
    summary: str
    weight: float
    duration: float
    annotation: Annotation
    distance: float

    @staticmethod
    def from_dict(obj: Any) -> 'Leg':
        _steps = obj.get("steps")
        _summary = str(obj.get("summary"))
        _weight = float(obj.get("weight"))
        _duration = float(obj.get("duration"))
        _annotation = Annotation.from_dict(obj.get("annotation"))
        _distance = float(obj.get("distance"))
        return Leg(_steps, _summary, _weight, _duration, _annotation, _distance)
    

@dataclass
class Route:
    geometry: str
    legs: List[Leg]
    weight_name: str
    weight: float
    duration: float
    distance: float

    @staticmethod
    def from_dict(obj: Any) -> 'Route':
        _geometry = str(obj.get("geometry"))
        _legs = [Leg.from_dict(y) for y in obj.get("legs")]
        _weight_name = str(obj.get("weight_name"))
        _weight = float(obj.get("weight"))
        _duration = float(obj.get("duration"))
        _distance = float(obj.get("distance"))
        return Route(_geometry, _legs, _weight_name, _weight, _duration, _distance)


@dataclass
class Waypoint:
    hint: str
    distance: float
    name: str
    location: List[float]

    @staticmethod
    def from_dict(obj: Any) -> 'Waypoint':
        _hint = str(obj.get("hint"))
        _distance = float(obj.get("distance"))
        _name = str(obj.get("name"))
        _location = list(map(float, obj.get("location")))
        return Waypoint(_hint, _distance, _name, _location)
    

@dataclass
class ORSMApiResult:
    code: str
    routes: List[Route]
    waypoints: List[Waypoint]

    @staticmethod
    def from_dict(obj: Any) -> 'ORSMApiResult':
        _code = str(obj.get("code"))
        _routes = [Route.from_dict(y) for y in obj.get("routes")]
        _waypoints = [Waypoint.from_dict(y) for y in obj.get("waypoints")]
        return ORSMApiResult(_code, _routes, _waypoints)


# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
