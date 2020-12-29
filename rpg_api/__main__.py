#!/usr/bin/env python3
from flask.logging import default_handler
from flask import request, g
import logging
import sys
import connexion
import os
import config
from dotenv import load_dotenv
from rpg_api.debugger import initialize_flask_server_debugger_if_needed

load_dotenv()
mode = os.environ.get('MODE')
initialize_flask_server_debugger_if_needed(mode)
APP_NAME = "RPG_API"

options = {"swagger_ui": mode != "PRODUCTION"}
app = connexion.App(APP_NAME, specification_dir='rpg_api/swagger/', options=options)
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
from config import CONFIG

# DB
from rpg_api.models import database, init_models, User, Inventory, Lootbox
db_url = 'sqlite:///rpg_api/test/CI.db' if mode == "CI" else os.environ.get('DATABASE_URL')
flask_app.config['DATABASE'] = db_url
database.init_app(flask_app)
init_models(flask_app)


# adding api last to sort import 
app.add_api('swagger.yaml', arguments={'title': 'RPG API'}, pythonic_params=True)

# adding json encoder
from rpg_api import encoder
flask_app.json_encoder = encoder.JSONEncoder

# get user before each request
@flask_app.before_request
def get_or_create_user():
    username = request.view_args.get("user")
    query = User.select().where(User.name == username)
    if query.exists():
        user = query.get()
    else:
        user = User.create(name=username)
        i = Inventory.create(user=user)
        for _ in range(CONFIG["start_lootboxes"]):
            i.add_item(Lootbox(rarety=CONFIG["lootboxes_rarety"]["common"]))
    g.user = user

if __name__ == '__main__':
    app.run(port=8080)
