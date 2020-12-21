import peewee
from rpg_api.models import database, peewee_signals
from rpg_api.models.user import User


class Inventory(database.Model, peewee_signals.Model):
    user = peewee.ForeignKeyField(User, backref='inventory')

    def __unicode__(self):
        return "{} Inventory".format(self.user)

    class Meta:
        db_table = "inventories"
