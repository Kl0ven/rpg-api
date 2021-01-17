from rpg_api.dungeon.effects.base_effect import Base_Effect
import random
import config


class Protection(Base_Effect):
    def __init__(self, *args, **kwargs):
        super(Protection, self).__init__(*args, **kwargs)
        self.name = "Protection"
        self.power = config.CONFIG["effects_power"]["protection"]

    def start(self):
        super(Protection, self).start()
        self.buff = int(self.user.deff * self.power)
        if self.buff == 0:
            self.buff = 30
        old_stats = str(self.user)
        self.user.deff += self.buff
        self.reporter.log("{} => {}".format(old_stats, str(self.user)))

    def stop(self):
        super(Protection, self).stop()
        old_stats = str(self.user)
        self.user.deff -= self.buff
        self.reporter.log("{} => {}".format(old_stats, str(self.user)))

    def update(self):
        super(Protection, self).update()
