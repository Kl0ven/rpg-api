import peewee
from rpg_api.models.item import Item
from config import CONFIG

class Loot(Item):
    type = peewee.IntegerField()
    image_url = peewee.TextField()
    rarety = peewee.IntegerField()

    def __unicode__(self):
        return self.name

    def get_type_name(self):
        return CONFIG['invert_loot_type'][self.type]

    def get_rarety_name(self):
            return CONFIG['invert_lootboxes_rarety'][self.rarety]

    def to_dict(self):
        return {
            "name": self.name,
            "slot": self.slot,
            "type": {
                "value": self.type,
                "name": self.get_type_name()
            },
            "rarety": {
                "value": self.rarety,
                "name": self.get_rarety_name()
            }
        }



    class Meta:
        db_table = "loots"
