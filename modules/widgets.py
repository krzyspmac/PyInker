from PIL import Image, ImageDraw, ImageFont
import textwrap
from .general import Rect
from .general import text_wrap
from .modules_interfaces import *
import logging

class TextWidget(WidgetInterface):

    text = ""
    font = None
    color = (0)
    
    def __init__(self) -> None:
        super().__init__()
        self.__logger = logging.getLogger('TextWidget')
        pass

    # WidgetInterfaces

    def draw(self, image: Image, drawObject):
        self.draw_me(image, drawObject)
        pass

    # TextWidget

    def set_text(self, text: str):
        self.text = text
        pass

    def get_text(self) -> str:
        return self.text

    def set_font(self, font):
        self.font = font
        self.__logger.info("font = %s", font)
        pass

    def set_text_color(self, color):
        self.color = color
        self.__logger.info("color = %s", color)
        pass

    def draw_me(self, image: Image, drawObject):
        drawObject.rectangle(self.bounds.shape, fill=(255), outline=(0))
        wrapper = textwrap.TextWrapper(width=self.bounds.width) 
        description_wrapped = text_wrap(self.text, self.font, drawObject, self.bounds.width, self.bounds.height)
        drawObject.text( (self.bounds.x, self.bounds.y), description_wrapped, font=self.font, fill=self.color)
