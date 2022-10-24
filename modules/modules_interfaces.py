class ModuleManagerInterface:

    def register_module(self, module_name, module):
        """Register a module for future use."""
        pass

    def setup_modules(self, configuration):
        pass

    pass # ModuleManagerInterface

class ModuleInterface:
    """Define an interface for a module. Each module will be loaded by the main application and it will have the opprotunity to register itself for updates."""

    def setup(self, configuration):
        pass

    pass # ModuleInterface
