# -*- encoding:utf-8 -*-
import os

global APP_PATH
global APP_TITLE
global APP_SIZE_X
global APP_SIZE_Y
global APP_VERSION
# Take fixed file path, and not the relative file path
APP_PATH = os.path.dirname(os.path.realpath(__file__))

APP_VERSION = "0.1.2"
APP_TITLE = "Detector Codebare"
APP_SIZE_X = 1000
APP_SIZE_Y = 600
FONT_STYLE = ("Roboto", 18)