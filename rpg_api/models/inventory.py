import peewee
from rpg_api.models import database, peewee_signals
from rpg_api.models.user import User
from config import CONFIG


class Inventory(database.Model, peewee_signals.Model):
    user = peewee.ForeignKeyField(User, backref='inventory')
    next_slot = peewee.IntegerField(default=1)

    def __unicode__(self):
        return "{} Inventory".format(self.user)

    def add_item(self, item):
        from rpg_api.models.lootbox import Lootboxe
        item.slot = self.next_slot
        self.next_slot += 1
        item.inventory = self
        if isinstance(item, Lootboxe):
            item.name = "{} Lootboxe".format(
                CONFIG["invert_lootboxes_rarety"][item.rarety].capitalize())
        self.save()
        item.save()
    class Meta:
        db_table = "inventories"
