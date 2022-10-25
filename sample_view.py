import os
from sre_constants import NOT_LITERAL
import time
from PIL import Image, ImageDraw, ImageFont
from modules.general import FontList
from modules.general import ColorList
from modules.general import Rect
from modules.widgets import TextWidget
from modules.widgets import ViewInterface
import yaml
from yaml import load, dump
from yaml import Loader, Dumper

class SampleView(ViewInterface):

    # ViewInterface

    def setup(self):
        super().setup()
        self._setup()
        pass

    def draw(self, image, draw):
        self._draw(image, draw)
        pass

    # Sample View

    def _setup(self):
        self._widget = TextWidget()
        self._widget.set_bounds(Rect(100, 100, 400, 200))
        self._widget.set_font(
            FontList.get_font("Default").create(25)
        )
        self._widget.set_text_color(
            ColorList.get_color("Red").rgb
        )

        pass

    def _draw(self, image, draw):
        self._widget.set_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum")
        self._widget.draw(draw)
        pass

    pass # SampleView