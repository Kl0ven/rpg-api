import logging
from rpg_api.dungeon.hero import Hero
from rpg_api.dungeon.room import Room
from config import CONFIG
logger = logging.getLogger('RPG_API.dungeon')


class Dungeon(object):
    def __init__(self, users, reporter):
        # planning on coop, so heros is a list
        self.heros = [Hero.create_hero_from_user(user, reporter) for user in users]
        self.reporter = reporter

    def crawl(self):
        i = 0
        self.reporter.log("Entering dungeon", self.heros)
        alive_heros = self.heros
        while len(alive_heros) != 0:
            i += 1

            # generate rooms
            r = Room(self.reporter, i)
            # add hero to room 
            r.add_heros(alive_heros)
            # fight => Room clear or Dead
            clear = r.fight()

            # wind_down
            alive_heros = [h for h in self.heros if not h.is_dead_or_fleeing()]

            for h in alive_heros:
                h.health += CONFIG["btw_rooms_regen"]
                h.room_cleared += 1
                self.reporter.log("Rest and gain {} health".format(CONFIG["btw_rooms_regen"]), h)
        result = {}
        for h in self.heros:
            result[h.name] = (h.room_cleared, h.fleeing, h.health)
        return result
        
