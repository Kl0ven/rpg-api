#!/usr/bin/env python3
import connexion
import os
from rpg_api import encoder
from rpg_api.models.db import database, init_models
from dotenv import load_dotenv
load_dotenv()
mode = os.environ.get('MODE')

options = {"swagger_ui": mode != "PRODUCTION"}
app = connexion.App(__name__, specification_dir='./swagger/', options=options)
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'RPG API'}, pythonic_params=True)


flask_app = app.app
db_url = 'sqlite:///:memory:' if mode == "CI" else os.environ.get('DATABASE_URL')
flask_app.config['DATABASE'] = db_url
database.init_app(flask_app)
init_models(flask_app)

if __name__ == '__main__':
    app.run(port=8080)
