import peewee
from rpg_api.models import database, peewee_signals
import datetime
from config import CONFIG

class User(database.Model, peewee_signals.Model):
    name = peewee.CharField()
    created = peewee.DateTimeField(default=datetime.datetime.now)
    balance = peewee.DecimalField(default=CONFIG["start_money"], max_digits=20, decimal_places=2)

    def __str__(self):
        return "User ({})".format(self.name)

    def __unicode__(self):
        return str(self)
    
    def __repr__(self):
        return str(self)

    class Meta:
        db_table = "users"
