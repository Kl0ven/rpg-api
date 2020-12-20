#!/usr/bin/env python3
import connexion
import os
from rpg_api import encoder
from rpg_api.models.db import database
from dotenv import load_dotenv
load_dotenv()
mode = os.environ.get('MODE')

options = {"swagger_ui": mode != "PRODUCTION"}
app = connexion.App(__name__, specification_dir='./swagger/', options=options)
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'RPG API'}, pythonic_params=True)


flask_app = app.app
flask_app.config['DATABASE'] = os.environ.get('DATABASE_URL')
database.init_app(flask_app)

if __name__ == '__main__':
    app.run(port=8080)
