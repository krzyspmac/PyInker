from email.mime import base
from ..modules_manager import ModuleManager
from .mod_graphs import ModuleGraphs
import os

ModuleManager.shared().register_module(
    os.path.basename(os.path.dirname(__file__)), 
    ModuleGraphs()
)
