# -*- encoding:utf-8 -*-
import os

global APP_PATH
global APP_TITLE
global APP_SIZE_X
global APP_SIZE_Y
# Take fixed file path, and not the relative file path
APP_PATH = os.path.dirname(os.path.realpath(__file__))

APP_TITLE = "Detector Codebare"
APP_SIZE_X = 600
APP_SIZE_Y = 400