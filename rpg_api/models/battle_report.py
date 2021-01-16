import peewee
from rpg_api.models import database, peewee_signals


class Battle_report(database.Model, peewee_signals.Model):

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "battle_report"
