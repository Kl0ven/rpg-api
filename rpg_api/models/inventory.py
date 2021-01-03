import peewee
from rpg_api.models import database, peewee_signals
from rpg_api.models.user import User
from config import CONFIG


class Inventory(database.Model, peewee_signals.Model):
    user = peewee.ForeignKeyField(User, backref='inventory')
    next_slot = peewee.IntegerField(default=1)
    loot_model = None
    lootbox_model = None

    @classmethod
    def set_models(cls, models):
        cls.loot_model = models['Loot']
        cls.lootbox_model = models['Lootbox']

    def __unicode__(self):
        return "{} Inventory".format(self.user)

    def add_item(self, item):
        from rpg_api.models.lootbox import Lootbox
        item.slot = self.next_slot
        self.next_slot += 1
        item.inventory = self
        if isinstance(item, Lootbox):
            item.name = "{} Lootbox".format(
                CONFIG["invert_lootboxes_rarety"][item.rarety].capitalize())
        self.save()
        item.save()

    def open_lootbox(self, lootbox):
        lootbox_price = lootbox.get_price()
        if self.user.balance >= lootbox_price: 
            self.user.balance -= lootbox_price
            self.user.save()
            lootbox.delete_instance()
            return True
        else:
            return False
    
    def get_loots(self):
        return list(self.loot_set.select().order_by(self.loot_model.rarety.desc()))

    def get_lootboxes(self):
        return list(self.lootbox_set.select().order_by(self.lootbox_model.rarety.desc()))

    def get_selected_armor(self):
        armor = self.loot_set.select().where(self.loot_model.selected == True, self.loot_model.type == CONFIG["loot_type"]["armor"])
        if armor.exists():
            return armor.get()
        else:
            return None

    def get_selected_potions(self):
        return list(self.loot_set.select().where(self.loot_model.selected == True, self.loot_model.type == CONFIG["loot_type"]["potion"]))

    def get_selected_weapon(self):
        weapon = self.loot_set.select().where(self.loot_model.selected == True, self.loot_model.type << CONFIG['weapon'])
        if weapon.exists():
            return weapon.get()
        else:
            return None

    class Meta:
        db_table = "inventories"
