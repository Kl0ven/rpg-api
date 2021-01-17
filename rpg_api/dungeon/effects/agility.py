from rpg_api.dungeon.effects.base_effect import Base_Effect
import random
import config


class Agility(Base_Effect):
    def __init__(self, *args, **kwargs):
        super(Agility, self).__init__(*args, **kwargs)
        self.name = "Agility"
        self.power = config.CONFIG["effects_power"]["agility"]

    def start(self):
        super(Agility, self).start()
        self.buff = random.randrange(*self.power)
        old_stats = str(self.user)
        self.user.crit_chance += self.buff
        self.reporter.log("{} => {}".format(old_stats, str(self.user)))

    def stop(self):
        super(Agility, self).stop()
        old_stats = str(self.user)
        self.user.deff -= self.buff
        self.reporter.log("{} => {}".format(old_stats, str(self.user)))

    def update(self):
        super(Agility, self).update()
