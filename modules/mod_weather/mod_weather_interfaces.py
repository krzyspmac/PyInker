import datetime

class ModuleWeatherItem:
    dt: datetime
    temp: float
    temp_feels: float

    def __repr__(self):
        return "ModuleWeatherItem("             \
        + "dt=" + str(self.dt)                  \
        + ", temp=" + str(self.temp)            \
        + ", feel_like=" + str(self.temp_feels) \
        + ")"

    pass # ModuleWeatherItem

class ModuleWeatherData:

    # Items; can be days, minutes, hours
    items: [ModuleWeatherItem]

    pass # ModuleWeatherData

class ModuleWeatherConnectorInterface:
    """Defines the interface for the various weather connectors"""

    def setup(self, configuration):
        """Recieve the configuration from yaml"""
        pass

    def download(self, lambda_result):
        """Perform the data download. Return the result to the lambda_result
           passing one parameter that is of the wanted type
        """
        pass

    pass # ModuleWeatherConnector