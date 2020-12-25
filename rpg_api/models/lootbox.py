import peewee
from rpg_api.models.item import Item


class Lootbox(Item):
    rarety = peewee.IntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "lootboxes"
