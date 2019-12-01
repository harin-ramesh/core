import os
import importlib

def  get_settings():
    SETTINGS = os.environ['SETTINGS_MODULE']
    return importlib.import_module(SETTINGS)
settings = get_settings()

