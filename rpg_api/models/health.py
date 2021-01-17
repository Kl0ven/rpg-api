import peewee
from rpg_api.models import database, peewee_signals
from rpg_api.models.user import User
from config import CONFIG
from numpy import interp
from datetime import datetime, timedelta

class Health(database.Model, peewee_signals.Model):
    user = peewee.ForeignKeyField(User, backref='health')
    health = peewee.IntegerField(default=CONFIG['max_health'])
    health_start = peewee.IntegerField(null=True)
    health_end = peewee.IntegerField(null=True)
    start_time = peewee.DateTimeField(null=True)
    end_time = peewee.DateTimeField(null=True)

    def set_health_decay(self, end_time):
        self.health_start = self.health
        self.health_end = 0
        self.start_time = datetime.now()
        self.end_time = end_time

    def update_health(self):
        if self.health_start is not None and self.health_end is not None and self.start_time is not None and self.end_time is not None:
            now = datetime.now()
            if now > self.end_time:
                self.health = self.health_end
                if self.health == self.health_end and self.health != CONFIG['max_health']:
                    self.health_start = 0
                    self.health_end = CONFIG["max_health"]
                    self.start_time = self.end_time
                    minutes_of_regen = int(CONFIG["max_health"] / CONFIG['natural_regen_rate'])
                    self.end_time += timedelta(minutes=minutes_of_regen)
                    self.__update()
                else:
                    self.health_start = None
                    self.health_end = None
                    self.start_time = None
                    self.end_time = None
            else: 
                self.__update()
            self.save()

    def __update(self):
        time_range = [self.start_time.timestamp(), self.end_time.timestamp()]
        self.health = interp(datetime.now().timestamp(), time_range, [self.health_start, self.health_end])

    def __str__(self):
        return "({}) Health: {}".format(self.user.name, self.health)

    def __unicode__(self):
        return str(self)

    def __repr__(self):
        return str(self)

    class Meta:
        db_table = "health"
