import sys
import os
from peewee import *  # no other way to reach playhouse :(
from playhouse import flask_utils as peewee_flask_utils
from playhouse import signals as peewee_signals

# DB connection
database = peewee_flask_utils.FlaskDB()

path = os.path.dirname(os.path.abspath(__file__))
models = []
for py in [f[:-3] for f in os.listdir(path) if f.endswith('.py') and f not in ['__init__.py', 'db.py']]:
    mod = __import__('.'.join([__name__, py]), fromlist=[py])
    classes = [getattr(mod, x) for x in dir(mod) if isinstance(getattr(mod, x), type)]
    for cls in classes:
        models.append(cls)
        setattr(sys.modules[__name__], cls.__name__, cls)


def init_models(app):
    app.before_first_request(_init_models)


def _init_models():
    db = database.database
    db.create_tables(models)
    db.close()
