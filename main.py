import os
import time
import curses
from threading import Thread
from PIL import Image, ImageDraw, ImageFont
from modules.general import *
from modules.widgets import *
from display.display_waveshare import *
from configuration import Configuration
from modules.renderer import Renderer
from modules.modules_manager import ModuleManager
from modules.mod_main.mod_main import ModuleMainView

# Configuration
configuration: Configuration
modulesManager: ModuleManager
displayDevice: DisplayDeviceInterface
renderer: Renderer

def setup():
    """Setup the application, load configuration files, etc."""
    global configuration
    global modulesManager
    global renderer

    configuration = Configuration("config.yml")

    modulesManager = ModuleManager()
    modulesManager.load_modules()
    modulesManager.setup_modules(configuration=configuration)

    displayDevice = DisplayWaveshare()

    renderer = Renderer(
        width=configuration.screen["width"], 
        height=configuration.screen["height"], 
        background=ColorList.get_color("White"),
        displayDevice=displayDevice
        )
    pass

def draw():
    view = ModuleMainView()
    view.setup(renderer=renderer)
    view.draw(renderer.image, renderer.draw)
    renderer.image.show()
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

# curses.wrapper(main)