from PIL import Image, ImageDraw, ImageFont
import textwrap
from .general import Rect
from .general import text_wrap

class WidgetInterface:
    @property
    def bounds(self):
        print("getter method called")
        return self._bounds

    @bounds.setter
    def bounds(self, val):
        self._bounds = val

    def set_config(self, config: dict):
        """Receive the configuration. Each Widget can take something else from the configuration itself."""
        pass

    def set_bounds(self, bounds: Rect):
        """Sets bounds."""
        self.bounds = bounds
        pass

    def draw(self, drawObject):
        """Draws the widget"""
        pass

    pass # WidgetInterface

class ViewInterface:

    def setup(self):
        """A good point to setup the view."""
        pass

    def draw(self, image, draw):
        """Called by the main screen. You should draw the view. Some additional parameters can be passed so not all the screen is udpated all the time."""
        pass

    pass # ViewInterface

class TextWidget(WidgetInterface):

    text = ""
    font = None
    color = (0, 0, 0)

    # WidgetInterfaces

    def draw(self, drawObject):
        self.draw_me(drawObject)
        pass

    # TextWidget

    def set_text(self, text: str):
        self.text = text
        pass

    def set_font(self, font):
        self.font = font
        pass

    def set_text_color(self, color):
        self.color = color
        pass

    def draw_me(self, drawObject):
        drawObject.rectangle(self.bounds.shape, fill=(255, 255, 255), outline=(0, 0, 0))
        wrapper = textwrap.TextWrapper(width=self.bounds.width) 
        description_wrapped = text_wrap(self.text, self.font, drawObject, self.bounds.width, self.bounds.height)
        drawObject.text( (self.bounds.x, self.bounds.y), description_wrapped, font=self.font, fill=self.color)
