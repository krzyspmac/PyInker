import os
from sre_constants import NOT_LITERAL
import time
from PIL import Image, ImageDraw, ImageFont
from general import FontList
from general import ColorList
from general import Rect
from widgets import TextWidget
import yaml
from yaml import load, dump
from yaml import Loader, Dumper
from sample_view import SampleView

# Configuration
display = {'width': 320, 'height': 200}

def draw():
    image = Image.new("RGB", (display['width'], display['height']), color=ColorList.get_color("White").rgb)
    draw = ImageDraw.Draw(image)

    view = SampleView()
    view.setup()
    view.draw(image, draw)

    image.show()
    pass

with open("config.yml", "r") as stream:
    try:
        cfg = yaml.safe_load(stream)
        print(cfg["screen"])
        width = int(cfg["screen"]["width"])
        print(width)

        screen = cfg["screen"]
        display = {'width': int(screen["width"]), 'height': int(screen["height"])}

        FontList.from_config(cfg["fonts"])
        ColorList.from_config(cfg["colors"])
    except yaml.YAMLError as exc:
        print(exc)

draw()