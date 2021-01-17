from rpg_api.dungeon.effects.base_effect import Base_Effect
import random
import config


class Regeneration(Base_Effect):
    def __init__(self, *args, **kwargs):
        super(Regeneration, self).__init__(*args, **kwargs)
        self.name = "Regeneration"
        self.power = config.CONFIG["effects_power"]["regeneration"]

    def start(self):
        super(Regeneration, self).start()
        self.buff = random.randrange(*self.power)
        old_stats = str(self.user)
        self.user.health += self.buff
        self.reporter.log("{} => {}".format(old_stats, str(self.user)))

    def stop(self):
        super(Regeneration, self).stop()

    def update(self):
        super(Regeneration, self).update()
        old_stats = str(self.user)
        self.user.health += self.buff
        self.reporter.log("{} => {}".format(old_stats, str(self.user)))
