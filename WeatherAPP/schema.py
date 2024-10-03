import strawberry
import os
from dotenv import load_dotenv
import requests
from typing import List

load_dotenv()

FLOWISE_URL = os.getenv("FLOWISE_URL")
HEADERS = {"Authorization": os.getenv("FLOWISE_TOKEN")}
API_KEY = os.getenv("OPENWEATHER_API_KEY")


# schema and resolver about weather
@strawberry.type
class Wind:
    speed: float
    deg: int


@strawberry.type
class Clouds:
    all: int


@strawberry.type
class Weather:
    city: str
    main: str
    description: str
    temperature: float
    feelsLike: float
    tempMin: float
    tempMax: float
    pressure: int
    humidity: float
    seaLevel: int
    wind: Wind
    clouds: Clouds


def getWeather(city: str) -> Weather:
    """
    Function resolver to weather API call and data mapping
    """
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={API_KEY}&units=metric"
    )
    response = requests.get(url)
    data = response.json()

    wind = Wind(speed=data["wind"]["speed"], deg=data["wind"]["deg"])
    clouds = Clouds(all=data["clouds"]["all"])

    weather = Weather(
        city=data["name"],
        main=data["weather"][0]["main"],
        description=data["weather"][0]["description"],
        temperature=data["main"]["temp"],
        feelsLike=data["main"]["feels_like"],
        tempMin=data["main"]["temp_min"],
        tempMax=data["main"]["temp_max"],
        pressure=data["main"]["pressure"],
        humidity=data["main"]["humidity"],
        seaLevel=data["main"].get("sea_level", 0),
        wind=wind,
        clouds=clouds,
    )

    return weather


def getCurrentDay(timezone: str) -> str:
    """
    Function resolver to datetime API call and data mapping
    """
    url = f"https://worldtimeapi.org/api/timezone/{timezone}"
    response = requests.get(url)
    data = response.json()
    return data["datetime"]


def connectFlowise(message: str, history: List[str] = None) -> str:
    """
    Function resolver to Flowise API call and connection
    """
    if history is None:
        history = []
    payload = {"question": message}
    try:
        response = requests.post(FLOWISE_URL, json=payload, headers=HEADERS)
        response.raise_for_status()
        return response.json()["text"]
    except requests.exceptions.RequestException:
        return (
            "Sorry!, I cann't connect to the server right now. "
            "Please, try again later."
        )
    except Exception as e:
        return (
            f"Sorry! I can't connect to the server right now. "
            f"Please, try again later. Error: {e}"
       )


@strawberry.type
class Query:
    weather: Weather = strawberry.field(resolver=getWeather)
    date: str = strawberry.field(resolver=getCurrentDay)
    flowise: str = strawberry.field(resolver=connectFlowise)


schema = strawberry.Schema(query=Query)

