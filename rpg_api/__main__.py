#!/usr/bin/env python3
from flask.logging import default_handler
import logging
import sys
import connexion
import os
import config
from rpg_api import encoder
from dotenv import load_dotenv

load_dotenv()
mode = os.environ.get('MODE')

APP_NAME = "RPG_API"

options = {"swagger_ui": mode != "PRODUCTION"}
app = connexion.App(APP_NAME, specification_dir='rpg_api/swagger/', options=options)
app.app.json_encoder = encoder.JSONEncoder
flask_app = app.app


# logging
flask_app.logger.removeHandler(default_handler)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
flask_app.logger.addHandler(handler)
flask_app.logger.setLevel(logging.INFO if mode == "PRODUCTION" else logging.DEBUG)
flask_app.logger.info("Running in {} mode with {} log level".format(mode, logging.getLevelName(flask_app.logger.level)))

# Config
config.load_config()

# DB
from rpg_api.models import database, init_models
db_url = 'sqlite:///rpg_api/test/CI.db' if mode == "CI" else os.environ.get('DATABASE_URL')
flask_app.config['DATABASE'] = db_url
database.init_app(flask_app)
init_models(flask_app)


# adding api last to sort import 
app.add_api('swagger.yaml', arguments={'title': 'RPG API'}, pythonic_params=True)

if __name__ == '__main__':
    app.run(port=8080)
