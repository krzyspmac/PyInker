from ..modules_interfaces import ModuleInterface
from ..modules_manager import ModuleManager

class ModuleWeather(ModuleInterface):

    # ModuleInterface

    def setup(self, configuration):
        super().setup(configuration)
        pass

    # ModuleWeather

    def __repr__(self):
        return 'ModuleWeather!'

    pass # ModuleWeather
