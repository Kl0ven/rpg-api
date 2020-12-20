import peewee
from rpg_api.models import database, peewee_signals
import datetime


class Item(database.Model, peewee_signals.Model):
    title = peewee.CharField()
    content = peewee.TextField()
    members_only = peewee.BooleanField()
    created = peewee.DateTimeField(default=datetime.datetime.now)
    modified = peewee.DateTimeField()

    def __unicode__(self):
        return self.title

    class Meta:
        order_by = ('-created',)
        db_table = "items"
