from .mod_weather import ModuleWeatherConnectorInterface
import urllib.request, json
from threading import Thread
from threading import main_thread
import logging
import time

class OpenWeatherConnector(ModuleWeatherConnectorInterface):

    __key: str
    __thread: Thread
    __lambda_result: None

    def __init__(self) -> None:
        super().__init__()
        self.__logger = logging.getLogger('ModuleWeather')
        pass

    # ModuleWeatherConnectorInterface

    def setup(self, configuration):
        super().setup(configuration)
        self.__key = configuration["key"]
        self.__logger.info("OpenWeather API Key = %s", self.__key)

    def download(self, lambda_result):
        super().download(lambda_result)
        self.__lambda_result = lambda_result
        thread = Thread(target=self.__threaded)
        thread.start()
        pass

    # OpenWeatherConnector

    def __threaded(self):
        self.__logger.info("Threading starting")
        time.sleep(5)
        self.__logger.info("Threading waking")
        url_string = "https://api.openweathermap.org/data/2.5/forecast?id=524901&appid=" + self.__key
        with urllib.request.urlopen(url_string) as url:
            data = json.load(url)
            #print(data)
            #self.__logger.info("Threaded data = %s", data)
            self.__lambda_result(data)
        pass

    pass # OpenWeatherConnector
