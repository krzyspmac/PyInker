from urllib.request import Request
from .general import Rect
from PIL import Image, ImageDraw, ImageFont

class DisplayDeviceInterface:
    """Defines an interface for the physical device. All low-level functions should pass through a specific
       device back-end so that they're easy to be replaced.
       The RendererInterface works directly with the `DisplayDeviceInterface`.
    """

    def setup(self):
        """Perform the setup. Only once."""
        pass

    def init(self):
        """Called before the first display. Only once."""
        pass

    def deinit(self):
        """Deinitializes the view."""
        pass

    def pre_display(self):
        """Called before each frame update."""
        pass

    def clear(self):
        """Clears the viewport."""
        pass

    def sleep(self):
        """Puts the display to sleep if possible."""
        pass

    def display_full(self, image: Image):
        pass

    def display_partial(self, image: Image, bouds: Rect):
        pass

    pass # DisplayDeviceInterface

class RendererInterface:
    """Defines an interface for the renderer.
       The renderer should handle the refresh of the screen be it the full-screen refresh
       or a partial one. Multiple views, while being renderered, can register refresh requests
       and those should be he handled in order with no special processing for now.
       The only exception to the rull is the full screen refresh request which, in effect,
       should clear the refresh stack and just perform the full-screen refresh of the screen.
       """

    class RefreshRequest:
        """The refresh request with preferred bounds or none."""

        def __init__(self):
            self._frame = None
            pass

        def __init__(self, frame: Rect):
            self._frame = frame
            pass

        @property
        def frame(self):
            return self._frame

        @property
        def is_fullscreen(self):
            return self.frame is None

        pass # Request

    def __init__(self, displayDevice: DisplayDeviceInterface):
        self.__display = displayDevice
        pass

    def enqueue_refresh(self, refresh: RefreshRequest):
        """Enqueue the refresh request. Fullscreen refresh should clear the stack and, in theory,
           no new enqueue refresh requests should not be needed.
        """
        pass

    def display(self):
        """Perform the draw of the stored image & drawable taking into account the enqueued refresh requests."""
        pass
    
    @property
    def displayDevice(self):
        return self.__display

    pass # RendererInterface

class ModuleManagerInterface:
    """Denotes the default interface for the module manager.
    """

    def register_renderer(self, renderer: RendererInterface):
        self.__renderer = renderer
        pass

    def register_module(self, module_name, module):
        """Register a module for future use."""
        pass

    def setup_modules(self, configuration):
        """Setup modules by providing the YAML-parsed configuration."""
        pass

    @property
    def renderer(self):
        return self.__renderer

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

class ViewCoordinator:
    """Defines the interface for the coordinator that takes charge of
       view switching.
    """

    def setup(self, configuration, renderer: RendererInterface):
        pass

    def set_view_active(self, view):
        pass

    pass

class ViewInterface:
    """Defines the interface for a view.
       A View is defined by having access to the whole screens, is the sole
       receiver of the keyboard inputs. It is managed by the main
       coordinator that has the option to change the current view to another one.
    """

    def setup(self, renderer: RendererInterface, viewCoordinator: ViewCoordinator, configuration):
        """A good point to setup the view."""
        self.__renderer = renderer
        self.__coordinator = viewCoordinator
        self.__configuration = configuration
        pass

    def will_deactivate(self):
        """Called just before deactiation of the view."""
        pass

    def will_activate(self):
        """Called just before activation of the view."""
        pass

    def did_deactivate(self):
        """Called just after deactivation."""
        pass

    def did_activate(self):
        """Called just after activation."""
        pass

    def draw(self, image, draw):
        """Called by the main screen. You should draw the view. Some additional parameters
           can be passed so not all the screen have to be udpated all the time.
        """
        pass

    @property
    def renderer(self):
        """Return the current renderer."""
        return self.__renderer

    @property
    def coordinator(self):
        """Return the current view coordinatator."""
        return self.__coordinator
    
    @property
    def configuration(self):
        """Returns the configuration passed to this view"""
        return self.__configuration

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
