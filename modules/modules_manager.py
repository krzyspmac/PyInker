import os
import importlib
from .modules_interfaces import ModuleManagerInterface
from .modules_interfaces import ModuleInterface

_sharedModuleManager = None

class ModuleManager(ModuleManagerInterface):
    modules = {}

    # ModuleManagerInterface

    def register_module(self, module_name, module: ModuleInterface):
        super().register_module(module_name, module)
        self.modules[module_name] = module
        pass

    def setup_modules(self, configuration):
        super().setup_modules(configuration)

        print(self.renderer)

        mod_configs = configuration.raw["modules"]
        for module in self.modules:
            this_mod_config = {}
            if module in mod_configs:
                this_mod_config = mod_configs[module]
                pass
            self.modules[module].setup(this_mod_config)
            pass
        pass

    # ModuleManager

    def __init__(self):
        global _sharedModuleManager
        _sharedModuleManager = self
        pass

    def load_modules(self):
        for file in os.listdir(os.path.dirname(__file__)):
            if file.startswith("mod_"):
                cmd = "from ." + file + "." + file + " import *"
                exec(cmd)
        pass


    @staticmethod
    def shared():
        return _sharedModuleManager

    pass # ModuleManager

_sharedModuleManager = ModuleManager()
