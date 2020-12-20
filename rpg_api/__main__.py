#!/usr/bin/env python3
import connexion
import os
from rpg_api import encoder
mode = os.environ.get('MODE')

options = {"swagger_ui": mode != "PRODUCTION"}
print(options)
app = connexion.App(__name__, specification_dir='./swagger/', options=options)
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'RPG API'}, pythonic_params=True)


if __name__ == '__main__':
    app.run(port=8080)
