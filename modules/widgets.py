from PIL import Image, ImageDraw, ImageFont
import textwrap
from .general import Rect
from .general import text_wrap
from .modules_interfaces import *

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

    def get_text(self) -> str:
        return self.text

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
