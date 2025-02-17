from .mod_weather_interfaces import *
import urllib.request, json
from threading import Thread
from threading import main_thread
import logging
import time
from datetime import datetime
import array

class OpenWeatherConnector(ModuleWeatherConnectorInterface):

    __key: str
    __lat: float
    __lon: float
    __thread: Thread
    __lambda_result: None

    def __init__(self) -> None:
        super().__init__()
        self.__logger = logging.getLogger('OpenWeatherConnector')
        pass

    # ModuleWeatherConnectorInterface

    def setup(self, configuration):
        super().setup(configuration)
        self.__logger.info("Configuration = %s", configuration)
        self.__key = configuration["key"]
        self.__lat = configuration["lat"]
        self.__lon = configuration["lon"]
        self.__logger.info("OpenWeather API Key = %s", self.__key)

    def download(self, lambda_result):
        self.__logger.info("OpenWeather API downlaod starting...")
        super().download(lambda_result)
        self.__lambda_result = lambda_result
        thread = Thread(target=self.__threaded)
        thread.start()
        pass

    # OpenWeatherConnector

    def __threaded(self):
        self.__logger.info("OpenWeather API thread starting...")
        self.__logger.info("OpenWeather API thread waiting...")
        url_string = "https://api.openweathermap.org/data/2.5/forecast?id=524901&appid=" + self.__key + "&&units=metric" + "&lat=" + str(self.__lat) + "&lon=" + str(self.__lat)
        self.__logger.info("OpenWeather API loading url %s", url_string)
        with urllib.request.urlopen(url_string) as url:
            data = json.load(url)
            self.__lambda_result(self.__convert(data))
        time.sleep(60)
        pass

    def __convert(self, data) -> ModuleWeatherData:
        result = ModuleWeatherData()
        self.__logger.info("OpenWeather API data convertion...")

        converted_list = []

        for item in data["list"]:
            dt = item["dt"]

            converted_item = ModuleWeatherItem()
            converted_item.dt = datetime.utcfromtimestamp(dt)

            main = item["main"]
            converted_item.temp = main["temp"]
            converted_item.temp_feels = main["feels_like"]

            self.__logger.info("dt = %s", converted_item)

            converted_list.append(converted_item)
            pass # item loop

        result.items = converted_list
        
        return result

    pass # OpenWeatherConnector
