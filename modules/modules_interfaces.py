from .general import Rect

class ModuleManagerInterface:
    """Denotes the default interface for the module manager.
    """

    def register_module(self, module_name, module):
        """Register a module for future use."""
        pass

    def setup_modules(self, configuration):
        """Setup modules by providing the YAML-parsed configuration."""
        pass

    pass # ModuleManagerInterface

class ModuleInterface:
    """Define an interface for a module. 
       A module is a piece of code that is automatically loaded
       by the module manager. Then the module has the option to
       register itself for periodic, scheduled updates or setup
       any other module-specific jobs.
    """

    def setup(self, configuration):
        pass

    pass # ModuleInterface

class ViewInterface:
    """Defines the interface for a view.
       A View is defined by having access to the whole screens, is the sole
       receiver of the keyboard inputs. It is managed by the main
       coordinator that has the option to change the current view to another one.
    """

    def setup(self):
        """A good point to setup the view."""
        pass

    def draw(self, image, draw):
        """Called by the main screen. You should draw the view. Some additional parameters can be passed so not all the screen is udpated all the time."""
        pass

    pass # ViewInterface

class WidgetInterface:
    """Defines the widget interface.
       A widget is defined by existing within a view, taking a specific amount
       of it defined by the bounds. A widget has the option to draw itself.
    """
    @property
    def bounds(self):
        print("getter method called")
        return self._bounds

    @bounds.setter
    def bounds(self, val):
        self._bounds = val

    def set_config(self, config: dict):
        """Receive the configuration.
           Each Widget can take something else from the configuration itself.
        """
        pass

    def set_bounds(self, bounds: Rect):
        """Sets bounds."""
        self.bounds = bounds
        pass

    def draw(self, drawObject):
        """Draws the widget"""
        pass

    pass # WidgetInterface
