import peewee
from rpg_api.models import database, peewee_signals
from rpg_api.models.user import User
import datetime
import uuid

class Battle_report(database.Model, peewee_signals.Model):
    br_id = peewee.UUIDField(unique=True, default=uuid.uuid4)
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


    def to_dict(self):
        if not hasattr(self, 'lootboxes'):
            self.lootboxes = []
        if not hasattr(self, 'first_opening'):
            self.first_opening = False
        return {
            "id": self.br_id,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "full_report_id": self.full_report,
            "fleeing": self.is_fleeing,
            "health": self.health,
            "money": self.money,
            "lootboxes": self.lootboxes,
            "first_opening": self.first_opening
        }
    class Meta:
        db_table = "battle_report"
