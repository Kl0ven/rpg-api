import peewee
from rpg_api.models.item import Item


class Loot(Item):
    type = peewee.IntegerField()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "loots"
