from PIL import Image, ImageDraw, ImageFont
import textwrap
from mod_general import Rect
from mod_general import text_wrap

class WidgetInterface:
    @property
    def bounds(self):
        print("getter method called")
        return self._bounds

    @bounds.setter
    def bounds(self, val):
        self._bounds = val

    def set_bounds(self, bounds: Rect):
        """Sets bounds."""
        self.bounds = bounds
        pass

    def draw(self, drawObject):
        """Draws the widget"""
        pass

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
