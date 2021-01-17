import peewee
from rpg_api.models import database, peewee_signals
from rpg_api.models.user import User
import datetime
import uuid

class Battle_report(database.Model, peewee_signals.Model):
    id = peewee.UUIDField(unique=True, default=uuid.uuid4)
    user = peewee.ForeignKeyField(User, backref='battle_reports')
    start_date = peewee.DateTimeField(default=datetime.datetime.now)
    end_date = peewee.DateTimeField()
    full_report = peewee.UUIDField()
    is_fleeing = peewee.BooleanField()
    health = peewee.IntegerField(default=0)
    lootboxes_data = peewee.TextField()
    money = peewee.IntegerField()
    opened = peewee.BooleanField(default=False)


    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "battle_report"
