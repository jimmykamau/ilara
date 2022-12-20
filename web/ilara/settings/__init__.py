import os


current_environment = os.getenv("ENVIRONMENT_SETTINGS")

if current_environment == "PRODUCTION":
    from ilara.settings.prod import *
elif current_environment == "DEVELOPMENT":
    from ilara.settings.develop import *
