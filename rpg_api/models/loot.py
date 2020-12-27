import peewee
from rpg_api.models.item import Item
from config import CONFIG

class Loot(Item):
    type = peewee.IntegerField()
    image_url = peewee.TextField()

    def __unicode__(self):
        return self.name

    def get_type_name(self):
        return CONFIG['invert_loot_type'][self.type]

    def to_dict(self):
        return {
            "name": self.name,
            "slot": self.slot,
            "image_url": self.image_url,
            "type": {
                "value": self.type,
                "name": self.get_type_name()
            }
        }

    class Meta:
        db_table = "loots"
