from connexion.apps.flask_app import FlaskJSONEncoder
import six
from rpg_api.models import database, peewee_signals

class JSONEncoder(FlaskJSONEncoder):
    include_nulls = False

    def default(self, o):
        if isinstance(o, database.Model):
            return o.to_dict()
        return FlaskJSONEncoder.default(self, o)
