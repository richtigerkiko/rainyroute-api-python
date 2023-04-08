from datetime import datetime
from typing import List
from typing import Any
from dataclasses import dataclass
import json

# https://json2csharp.com/code-converters/json-to-python MERCI!


@dataclass
class Astro:
    sunrise: str
    sunset: str
    moonrise: str
    moonset: str
    moon_phase: str
    moon_illumination: str
    is_moon_up: int
    is_sun_up: int

    @staticmethod
    def from_dict(obj: Any) -> 'Astro':
        _sunrise = str(obj.get("sunrise"))
        _sunset = str(obj.get("sunset"))
        _moonrise = str(obj.get("moonrise"))
        _moonset = str(obj.get("moonset"))
        _moon_phase = str(obj.get("moon_phase"))
        _moon_illumination = str(obj.get("moon_illumination"))
        _is_moon_up = int(obj.get("is_moon_up"))
        _is_sun_up = int(obj.get("is_sun_up"))
        return Astro(_sunrise, _sunset, _moonrise, _moonset, _moon_phase, _moon_illumination, _is_moon_up, _is_sun_up)


@dataclass
class Condition:
    text: str
    icon: str
    code: int

    @staticmethod
    def from_dict(obj: Any) -> 'Condition':
        _text = str(obj.get("text"))
        _icon = str(obj.get("icon"))
        _code = int(obj.get("code"))
        return Condition(_text, _icon, _code)


@dataclass
class Current:
    last_updated_epoch: int
    last_updated: str
    temp_c: float
    temp_f: float
    is_day: int
    condition: Condition
    wind_mph: float
    wind_kph: float
    wind_degree: int
    wind_dir: str
    pressure_mb: float
    pressure_in: float
    precip_mm: float
    precip_in: float
    humidity: int
    cloud: int
    feelslike_c: float
    feelslike_f: float
    vis_km: float
    vis_miles: float
    uv: float
    gust_mph: float
    gust_kph: float

    @staticmethod
    def from_dict(obj: Any) -> 'Current':
        if obj is None: return None
        
        _last_updated_epoch = int(obj.get("last_updated_epoch"))
        _last_updated = str(obj.get("last_updated"))
        _temp_c = float(obj.get("temp_c"))
        _temp_f = float(obj.get("temp_f"))
        _is_day = int(obj.get("is_day"))
        _condition = Condition.from_dict(obj.get("condition"))
        _wind_mph = float(obj.get("wind_mph"))
        _wind_kph = float(obj.get("wind_kph"))
        _wind_degree = int(obj.get("wind_degree"))
        _wind_dir = str(obj.get("wind_dir"))
        _pressure_mb = float(obj.get("pressure_mb"))
        _pressure_in = float(obj.get("pressure_in"))
        _precip_mm = float(obj.get("precip_mm"))
        _precip_in = float(obj.get("precip_in"))
        _humidity = int(obj.get("humidity"))
        _cloud = int(obj.get("cloud"))
        _feelslike_c = float(obj.get("feelslike_c"))
        _feelslike_f = float(obj.get("feelslike_f"))
        _vis_km = float(obj.get("vis_km"))
        _vis_miles = float(obj.get("vis_miles"))
        _uv = float(obj.get("uv"))
        _gust_mph = float(obj.get("gust_mph"))
        _gust_kph = float(obj.get("gust_kph"))
        return Current(_last_updated_epoch, _last_updated, _temp_c, _temp_f, _is_day, _condition, _wind_mph, _wind_kph, _wind_degree, _wind_dir, _pressure_mb, _pressure_in, _precip_mm, _precip_in, _humidity, _cloud, _feelslike_c, _feelslike_f, _vis_km, _vis_miles, _uv, _gust_mph, _gust_kph)


@dataclass
class Day:
    maxtemp_c: float
    maxtemp_f: float
    mintemp_c: float
    mintemp_f: float
    avgtemp_c: float
    avgtemp_f: float
    maxwind_mph: float
    maxwind_kph: float
    totalprecip_mm: float
    totalprecip_in: float
    totalsnow_cm: float
    avgvis_km: float
    avgvis_miles: float
    avghumidity: float
    daily_will_it_rain: int
    daily_chance_of_rain: int
    daily_will_it_snow: int
    daily_chance_of_snow: int
    condition: Condition
    uv: float

    @staticmethod
    def from_dict(obj: Any) -> 'Day':
        _maxtemp_c = float(obj.get("maxtemp_c"))
        _maxtemp_f = float(obj.get("maxtemp_f"))
        _mintemp_c = float(obj.get("mintemp_c"))
        _mintemp_f = float(obj.get("mintemp_f"))
        _avgtemp_c = float(obj.get("avgtemp_c"))
        _avgtemp_f = float(obj.get("avgtemp_f"))
        _maxwind_mph = float(obj.get("maxwind_mph"))
        _maxwind_kph = float(obj.get("maxwind_kph"))
        _totalprecip_mm = float(obj.get("totalprecip_mm"))
        _totalprecip_in = float(obj.get("totalprecip_in"))
        _totalsnow_cm = float(obj.get("totalsnow_cm"))
        _avgvis_km = float(obj.get("avgvis_km"))
        _avgvis_miles = float(obj.get("avgvis_miles"))
        _avghumidity = float(obj.get("avghumidity"))
        _daily_will_it_rain = int(obj.get("daily_will_it_rain"))
        _daily_chance_of_rain = int(obj.get("daily_chance_of_rain"))
        _daily_will_it_snow = int(obj.get("daily_will_it_snow"))
        _daily_chance_of_snow = int(obj.get("daily_chance_of_snow"))
        _condition = Condition.from_dict(obj.get("condition"))
        _uv = float(obj.get("uv"))
        return Day(_maxtemp_c, _maxtemp_f, _mintemp_c, _mintemp_f, _avgtemp_c, _avgtemp_f, _maxwind_mph, _maxwind_kph, _totalprecip_mm, _totalprecip_in, _totalsnow_cm, _avgvis_km, _avgvis_miles, _avghumidity, _daily_will_it_rain, _daily_chance_of_rain, _daily_will_it_snow, _daily_chance_of_snow, _condition, _uv)


@dataclass
class Hour:
    time_epoch: int
    time: datetime
    temp_c: float
    temp_f: float
    is_day: int
    condition: Condition
    wind_mph: float
    wind_kph: float
    wind_degree: int
    wind_dir: str
    pressure_mb: float
    pressure_in: float
    precip_mm: float
    precip_in: float
    humidity: int
    cloud: int
    feelslike_c: float
    feelslike_f: float
    windchill_c: float
    windchill_f: float
    heatindex_c: float
    heatindex_f: float
    dewpoint_c: float
    dewpoint_f: float
    will_it_rain: int
    chance_of_rain: int
    will_it_snow: int
    chance_of_snow: int
    vis_km: float
    vis_miles: float
    gust_mph: float
    gust_kph: float
    uv: float

    @staticmethod
    def from_dict(obj: Any) -> 'Hour':
        _time_epoch = int(obj.get("time_epoch"))
        _time = datetime.strptime(obj.get("time"), '%Y-%m-%d %H:%M')
        _temp_c = float(obj.get("temp_c"))
        _temp_f = float(obj.get("temp_f"))
        _is_day = int(obj.get("is_day"))
        _condition = Condition.from_dict(obj.get("condition"))
        _wind_mph = float(obj.get("wind_mph"))
        _wind_kph = float(obj.get("wind_kph"))
        _wind_degree = int(obj.get("wind_degree"))
        _wind_dir = str(obj.get("wind_dir"))
        _pressure_mb = float(obj.get("pressure_mb"))
        _pressure_in = float(obj.get("pressure_in"))
        _precip_mm = float(obj.get("precip_mm"))
        _precip_in = float(obj.get("precip_in"))
        _humidity = int(obj.get("humidity"))
        _cloud = int(obj.get("cloud"))
        _feelslike_c = float(obj.get("feelslike_c"))
        _feelslike_f = float(obj.get("feelslike_f"))
        _windchill_c = float(obj.get("windchill_c"))
        _windchill_f = float(obj.get("windchill_f"))
        _heatindex_c = float(obj.get("heatindex_c"))
        _heatindex_f = float(obj.get("heatindex_f"))
        _dewpoint_c = float(obj.get("dewpoint_c"))
        _dewpoint_f = float(obj.get("dewpoint_f"))
        _will_it_rain = int(obj.get("will_it_rain"))
        _chance_of_rain = int(obj.get("chance_of_rain"))
        _will_it_snow = int(obj.get("will_it_snow"))
        _chance_of_snow = int(obj.get("chance_of_snow"))
        _vis_km = float(obj.get("vis_km"))
        _vis_miles = float(obj.get("vis_miles"))
        _gust_mph = float(obj.get("gust_mph"))
        _gust_kph = float(obj.get("gust_kph"))
        _uv = float(obj.get("uv"))
        return Hour(_time_epoch, _time, _temp_c, _temp_f, _is_day, _condition, _wind_mph, _wind_kph, _wind_degree, _wind_dir, _pressure_mb, _pressure_in, _precip_mm, _precip_in, _humidity, _cloud, _feelslike_c, _feelslike_f, _windchill_c, _windchill_f, _heatindex_c, _heatindex_f, _dewpoint_c, _dewpoint_f, _will_it_rain, _chance_of_rain, _will_it_snow, _chance_of_snow, _vis_km, _vis_miles, _gust_mph, _gust_kph, _uv)


@dataclass
class Forecastday:
    date: str
    date_epoch: int
    day: Day
    astro: Astro
    hour: List[Hour]

    @staticmethod
    def from_dict(obj: Any) -> 'Forecastday':
        _date = str(obj.get("date"))
        _date_epoch = int(obj.get("date_epoch"))
        _day = Day.from_dict(obj.get("day"))
        _astro = Astro.from_dict(obj.get("astro"))
        _hour = [Hour.from_dict(y) for y in obj.get("hour")]
        return Forecastday(_date, _date_epoch, _day, _astro, _hour)


@dataclass
class Forecast:
    forecastday: List[Forecastday]

    @staticmethod
    def from_dict(obj: Any) -> 'Forecast':
        _forecastday = [Forecastday.from_dict(
            y) for y in obj.get("forecastday")]
        return Forecast(_forecastday)


@dataclass
class Location:
    name: str
    region: str
    country: str
    lat: float
    lon: float
    tz_id: str
    localtime_epoch: int
    localtime: str

    @staticmethod
    def from_dict(obj: Any) -> 'Location':
        if obj is None:
            return None
        _name = obj.get("name")
        _region = obj.get("region")
        _country = obj.get("country")
        _lat = float(obj.get("lat"))
        _lon = float(obj.get("lon"))
        _tz_id = str(obj.get("tz_id"))
        _localtime_epoch = int(obj.get("localtime_epoch"))
        _localtime = str(obj.get("localtime"))
        return Location(_name, _region, _country, _lat, _lon, _tz_id, _localtime_epoch, _localtime)


@dataclass
class Query:
    custom_id: int
    q: str
    location: Location
    current: Current
    forecast: Forecast

    @staticmethod
    def from_dict(obj: Any) -> 'Query':
        _custom_id = int(obj.get("custom_id"))
        _q = str(obj.get("q"))
        _location = Location.from_dict(obj.get("location"))
        _current = Current.from_dict(obj.get("current"))
        _forecast = Forecast.from_dict(obj.get("forecast"))
        return Query(_custom_id, _q, _location, _current, _forecast)


@dataclass
class Bulk:
    query: Query

    @staticmethod
    def from_dict(obj: Any) -> 'Bulk':
        _query = Query.from_dict(obj.get("query"))
        return Bulk(_query)


@dataclass
class WeatherApiBulkResponse:
    bulk: List[Bulk]

    @staticmethod
    def from_dict(obj: Any) -> 'WeatherApiBulkResponse':
        _bulk = [Bulk.from_dict(y) for y in obj.get("bulk")]
        return WeatherApiBulkResponse(_bulk)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
