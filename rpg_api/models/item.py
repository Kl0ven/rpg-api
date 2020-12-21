import peewee
from rpg_api.models import database, peewee_signals
from rpg_api.models.inventory import Inventory


class Item(database.Model, peewee_signals.Model):
    slot = peewee.IntegerField()
    name = peewee.CharField()
    inventory = peewee.ForeignKeyField(Inventory, backref='item')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "items"
