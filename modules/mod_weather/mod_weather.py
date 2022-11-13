from ..modules_interfaces import ModuleInterface
from ..modules_manager import ModuleManager

import logging

class ModuleWeatherConnectorInterface:
    """Defines the interface for the various weather connectors"""

    def setup(self, configuration):
        """Recieve the configuration from yaml"""
        pass

    def download(self, lambda_result):
        """Performs the data download and parses it into the appropriate format"""
        pass

    pass # ModuleWeatherConnector

class ModuleWeather(ModuleInterface):

    __connector: ModuleWeatherConnectorInterface

    # ModuleInterface

    def __init__(self) -> None:
        super().__init__()
        self.__logger = logging.getLogger('ModuleWeather')
        pass

    def setup(self, configuration):
        super().setup(configuration)
        connector_name = configuration["conector"]
        self.__initialize_connector(connector_name, configuration)
        pass

    # ModuleWeather

    def __initialize_connector(self, connector_name: str, configuration):
        self.__logger.info("Connector name = %s", connector_name)

        from .mod_weather_connector_openweather import OpenWeatherConnector

        instance = eval(connector_name)()
        self.__logger.info("Connector instance = %s", instance)
        self.__connector = eval(connector_name)()
        self.__connector.setup(configuration)
        self.__download()
        pass

    def __download(self):
        self.__connector.download(self.__download_finish)
        pass

    def __download_finish(self, data):
        self.__logger.info("result = %s", data)
        self.__logger.info("download_done")
        pass

    def __repr__(self):
        return 'ModuleWeather!'

    pass # ModuleWeather
