import os
from sre_constants import NOT_LITERAL
import time
from PIL import Image, ImageDraw, ImageFont
from general import FontList
from general import ColorList
from general import Rect
from widgets import TextWidget
from configuration import Configuration

import yaml
from yaml import load, dump
from yaml import Loader, Dumper
from sample_view import SampleView
# from pynput.keyboard import Key, Listener
import curses
import os
import time
from threading import Thread

# Configuration
display = {'width': 320, 'height': 200}
configuration: Configuration

def setup():
    global configuration
    global display
    configuration = Configuration("config.yml")
    display = {'width': configuration.screen["width"], 'height': configuration.screen["height"]}
    pass

def draw():
    image = Image.new("RGB", (display['width'], display['height']), color=ColorList.get_color("White").rgb)
    draw = ImageDraw.Draw(image)

    view = SampleView()
    view.setup()
    view.draw(image, draw)

    image.show()
    pass

setup()
draw()

def threaded():
    time.sleep(1)
    print('This is from another thread')
    pass

def main(win):
    """The main event queue"""
    thread = Thread(target=threaded)
    thread.start()

    win.nodelay(True)
    key=""
    win.clear()                
    win.addstr("Detected key:")
    while 1:         
        time.sleep(1/60)
        print("Wait\r")
        try:                 
           key = win.getkey()         
           win.clear()                
           win.addstr("Detected key:")
           win.addstr(str(key)) 
           if key == os.linesep:
              break           
        except Exception as e:
           # No input   
           pass         

def main2():
    thread = Thread(target=threaded)
    thread.start()

    while 1:
        print("From main thread\n")
        time.sleep(0.3)
        pass
    pass

# main2()

curses.wrapper(main)