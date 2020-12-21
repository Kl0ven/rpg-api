import peewee
from rpg_api.models import database, peewee_signals
import datetime
from config import CONFIG

class User(database.Model, peewee_signals.Model):
    name = peewee.CharField()
    created = peewee.DateTimeField(default=datetime.datetime.now)
    balance = peewee.DecimalField(default=CONFIG["start_money"])

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "users"
