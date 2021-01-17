from rpg_api.dungeon.character import Character
import random
from config import CONFIG


class Mob(Character):
    def __init__(self, **kwargs):
        super(Mob, self).__init__(**kwargs)


    @staticmethod
    def create_mob(mobs, reporter):
        mob = random.choice(CONFIG['mobs'])
        mob_name = mob["name"]
        mobs[mob_name] += 1
        atk = random.randrange(*mob["atk"])
        deff = random.randrange(*mob["def"])
        health = random.randrange(*mob["health"])
        return Mob(health=health, atk=atk, deff=deff, potions=[], rep=reporter, name='{}{}'.format(mob_name.capitalize(), mobs[mob_name]))
