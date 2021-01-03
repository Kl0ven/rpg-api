import peewee
from rpg_api.models import database, peewee_signals
import datetime
from config import CONFIG
import logging

logger = logging.getLogger('RPG_API.UserModel')

class User(database.Model, peewee_signals.Model):
    name = peewee.CharField()
    created = peewee.DateTimeField(default=datetime.datetime.now)
    balance = peewee.DecimalField(default=CONFIG["start_money"], max_digits=20, decimal_places=2)
    status = peewee.IntegerField(default=CONFIG["status"]["Idle"])
    next_status = peewee.IntegerField(default=CONFIG["status"]["Idle"])
    next_status_time = peewee.DateTimeField(null=True)

    def __str__(self):
        return "User ({})".format(self.name)

    def __unicode__(self):
        return str(self)
    
    def __repr__(self):
        return str(self)

    def update_status(self):
        if self.next_status_time is not None:
            now = datetime.datetime.now()
            if now > self.next_status_time:
                self.next_status_time = None
                self.status = self.next_status
                self.save()

    def update_health(self):
        self.health.get().update_health()

    def get_health(self):
        return self.health.get().health

    def get_status(self):
        return {
            "value": self.status,
            "name": CONFIG["invert_status"][self.status]
        }

    def to_dict(self):
        inv = self.inventory.get()
        return {
            "health": self.get_health(),
            "status": self.get_status(),
            "selected_armor": inv.get_selected_armor(),
            "selected_potion": inv.get_selected_potions(),
            "selected_weapon": inv.get_selected_weapon(),
        }

    class Meta:
        db_table = "users"
