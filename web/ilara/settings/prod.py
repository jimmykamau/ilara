import os

from ilara.settings.base import *


DEBUG = os.getenv("DEBUG", default=False)