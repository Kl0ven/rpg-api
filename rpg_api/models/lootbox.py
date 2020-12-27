import peewee
from rpg_api.models.item import Item
from config import CONFIG

class Lootbox(Item):
    rarety = peewee.IntegerField()

    def __unicode__(self):
        return self.name

    def get_rarety_name(self):
        return CONFIG['invert_lootboxes_rarety'][self.rarety]

    def to_dict(self):
        return {
            "name": self.name,
            "slot": self.slot,
            "price": CONFIG['lootbox_price'][self.get_rarety_name()],
            "rarety": {
                "value": self.rarety,
                "name": self.get_rarety_name()
            }
        }

    def get_price(self):
        return CONFIG['lootbox_price'][self.get_rarety_name()]

    class Meta:
        db_table = "lootboxes"
