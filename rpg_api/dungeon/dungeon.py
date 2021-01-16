import logging
from rpg_api.dungeon.hero import Hero
from rpg_api.dungeon.room import Room
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

            break
            # wind_down
            alive_heros = [h for h in self.heros if not h.is_dead_or_fleeing()]
