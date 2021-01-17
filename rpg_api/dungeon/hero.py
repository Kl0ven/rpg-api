from rpg_api.dungeon.character import Character
import random
from config import CONFIG

class Hero(Character):
    def __init__(self, **kwargs):
        super(Hero, self).__init__(**kwargs)
        self.fleeing = False
        self.room_cleared = 1

    def is_dead_or_fleeing(self):
        if self.fleeing or self.health <0:
            return True
        self.fleeing = random.random() > CONFIG['fleeing_chance']
        if self.fleeing:
            self.reporter.log("Flew away", self)
        return self.health <= 0 or self.fleeing

    @staticmethod
    def create_hero_from_user(user, reporter):
        inv = user.to_dict()
        atk = 0 if inv["selected_weapon"] is None else inv["selected_weapon"].complexity_factor
        deff = 0 if inv["selected_armor"] is None else inv["selected_armor"].complexity_factor
        return Hero(health=inv["health"], atk=atk, deff=deff, potions=inv["selected_potion"], rep=reporter, name=user.name.capitalize())

