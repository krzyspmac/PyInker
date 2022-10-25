from email.mime import base
from ..modules_manager import ModuleManager
from .mod_main import ModuleMain
import os

ModuleManager.shared().register_module(
    os.path.basename(os.path.dirname(__file__)), 
    ModuleMain()
)
