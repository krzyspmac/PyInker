import os
import time
import curses
from threading import Thread
from PIL import Image, ImageDraw, ImageFont
from modules.general import FontList
from modules.general import ColorList
from modules.general import Rect
from modules.widgets import *
from configuration import Configuration
from modules.modules_manager import ModuleManager
from sample_view import SampleView

# Configuration
display = {'width': 320, 'height': 200}
configuration: Configuration
modulesManager: ModuleManager

def setup():
    """Setup the application, load configuration files, etc."""
    global configuration
    global display
    global modulesManager

    configuration = Configuration("config.yml")
    display = {'width': configuration.screen["width"], 'height': configuration.screen["height"]}

    modulesManager = ModuleManager()
    modulesManager.load_modules()
    modulesManager.setup_modules(configuration=configuration)
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
# draw()

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

# curses.wrapper(main)