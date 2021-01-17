from rpg_api.dungeon.effects.base_effect import Base_Effect
import random
import config

class Strenght(Base_Effect):
    def __init__(self, *args, **kwargs):
        super(Strenght, self).__init__(*args, **kwargs)
        self.name = "Strength"
        self.power = config.CONFIG["effects_power"]["strength"]

    def start(self):
        super(Strenght, self).start()
        self.buff = int(self.user.atk * self.power)
        if self.buff == 0:
            self.buff = 30
        old_stats = str(self.user)
        self.user.atk += self.buff
        self.reporter.log("{} => {}".format(old_stats, str(self.user)))

    def stop(self):
        super(Strenght, self).stop()
        old_stats = str(self.user)
        self.user.atk -= self.buff
        self.reporter.log("{} => {}".format(old_stats, str(self.user)))

    def update(self):
        super(Strenght, self).update()
