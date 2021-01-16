from rpg_api.dungeon.effects.base_effect import Base_Effect
import random
import config

class Strenght(Base_Effect):
    def __init__(self, *args, **kwargs):
        super(Strenght, self).__init__(*args, **kwargs)
        self.name = "Strength"

    def start(self):
        super(Strenght, self).start()

    def stop(self):
        super(Strenght, self).stop()

    def update(self):
        super(Strenght, self).update()
