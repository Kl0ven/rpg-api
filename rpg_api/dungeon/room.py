import logging
from rpg_api.dungeon.mob import Mob
from rpg_api.dungeon.hero import Hero
from config import CONFIG
logger = logging.getLogger('RPG_API.room')


class Room(object):
    def __init__(self, reporter, i):
        self.reporter = reporter
        self.room_num = i
        self.name = "Room_{}".format(i)
        self.mob_indice = dict.fromkeys([m['name'] for m in CONFIG['mobs']], 0)
        self.heros = []
        nb_mob = (i//CONFIG['mob_increment']) + 1
        self.mobs = [Mob.create_mob(self.mob_indice, reporter) for _ in range(nb_mob)]
    
    def __str__(self):
        return "Room {}".format(self.name)

    def __repr__(self):
        return str(self)

    def add_heros(self, heros):
        self.heros = heros
        self.reporter.log("Enter room {}".format(self.room_num), heros)

    def fight(self):
        self.__log_room()
        self.__roll_inititive()
        players = self.__sort_character_by_inititive()
        heros_alive = True
        mobs_alive = True
        turn = 1
        while heros_alive and mobs_alive:
            self.reporter.log("Start of turn {}".format(turn), self)
            self.reporter.sep(length=70)
            for p in players:
                if not p.is_alive():
                    continue
                self.reporter.log("Start his turn {}".format(turn), p)
                self.reporter.log(str(p))

                if isinstance(p, Hero):
                    ennemies = [m for m in self.mobs if m.is_alive()]
                else:
                    ennemies = [h for h in self.heros if h.is_alive()]
                p.turn(ennemies=ennemies)
                self.reporter.sep(length=20)

            heros_alive, mobs_alive = self.__compute_liveliness()
            turn += 1
        return mobs_alive

    def __compute_liveliness(self):
        heros_alive = any([h.is_alive() for h in self.heros])
        mobs_alive = any([m.is_alive() for m in self.mobs])
        if not heros_alive:
            self.reporter.log("All heros are dead", self)
        if not mobs_alive:
            self.reporter.log("All mobs are dead", self)
        return heros_alive, mobs_alive
            

    def __log_room(self):
        self.reporter.log("In the room there is:")
        self.reporter.sep()
        for m in self.mobs:
            self.reporter.log(str(m))
        self.reporter.sep()

    def __sort_character_by_inititive(self):
        players = self.mobs + self.heros
        players.sort(key=lambda p: p.initiative, reverse=True)
        self.reporter.sep()
        for p in players:
            self.reporter.log("Rolled {} in initiative (1d100)".format(p.initiative), p)
        self.reporter.sep()
        return players

    def __roll_inititive(self):
        self.reporter.log("Rolling initiative...", self)
        for m in self.mobs:
            m.roll_initiative()
        for h in self.heros:
            h.roll_initiative()
