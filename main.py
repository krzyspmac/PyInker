import os
from sre_constants import NOT_LITERAL
import time
from PIL import Image, ImageDraw, ImageFont
from mod_general import Rect
from mod_widgets import TextWidget
import yaml
from yaml import load, dump
from yaml import Loader, Dumper

# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Display
display = {'width': 1280, 'height': 800}

def draw():
    image = Image.new("RGB", (display['width'], display['height']), color=WHITE)
    draw = ImageDraw.Draw(image)

    widget = TextWidget()
    widget.set_bounds(Rect(100, 100, 400, 200))
    widget.set_font(
        ImageFont.truetype("fonts/Bitter-VariableFont_wght.ttf", 25)
    )
    widget.set_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum")
    widget.set_text_color(BLACK)
    widget.draw(draw)

    image.show()
    pass

with open("config.yml", "r") as stream:
    try:
        cfg = yaml.safe_load(stream)
        print(cfg["screen"])
        width = int(cfg["screen"]["width"])
        print(width)
    except yaml.YAMLError as exc:
        print(exc)

# print(cfg["screen"])

draw()