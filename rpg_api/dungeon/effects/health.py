from rpg_api.dungeon.effects.base_effect import Base_Effect
import random
import config


class Health(Base_Effect):
    def __init__(self, *args, **kwargs):
        super(Health, self).__init__(*args, **kwargs)
        self.name = "Health"
        self.power = config.CONFIG["effects_power"]["health"]
        self.one_shot_effect = True

    def start(self):
        super(Health, self).start()
        h = random.randrange(*self.power)
        old_stats = str(self.user)
        self.user.health += h
        self.reporter.log("{} => {}".format(old_stats, str(self.user)))

    def stop(self):
        pass

    def update(self):
        super(Health, self).update()
