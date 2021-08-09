import os
from os.path import join

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_FOLDER = join(ROOT_PATH, "config")
CONFIG_FILE = join(CONFIG_FOLDER, "conf.ini")

