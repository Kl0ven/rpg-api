import peewee
from rpg_api.models.item import Item
from config import CONFIG

class Lootbox(Item):
    rarety = peewee.IntegerField()

    def __unicode__(self):
        return self.name

    def get_rarety_name(self):
        return CONFIG['invert_lootboxes_rarety'][self.rarety]
    class Meta:
        db_table = "lootboxes"
