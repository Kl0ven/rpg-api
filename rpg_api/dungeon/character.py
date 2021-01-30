from config import CONFIG
import random 

class Character(object):
    POTION_STEP=0
    ACTION_STEP=1

    def __init__(self, name, rep, atk=2, deff=2, health=CONFIG["max_health"], potions=[]):
        self.atk = atk
        self.deff = deff
        self.potions = potions
        self.used_potions = []
        self.health = health
        self.initiative = None
        self.reporter = rep
        self.name = name
        self.crit_chance = CONFIG['crit']
        self.crit_power = CONFIG['crit_power']
        self.effects = []

    def __str__(self):
        return "{}: (health: {}, atk: {}, def: {}, crit: {}%)".format(self.name, self.health, self.atk, self.deff, self.crit_chance)

    def __repr__(self):
        return str(self)

    def roll_initiative(self):
        self.initiative = random.randrange(1, 101)

    def is_alive(self):
        return self.health > 0

    def turn(self, ennemies):
        self.update_effect()
        step = self.choose_step()
        if step == self.POTION_STEP:
            p = random.choice(self.potions)
            p.used = True
            self.potions.remove(p)
            self.used_potions.append(p)
            self.reporter.log("Choose to use a {}".format(p.name), self)
            effect = random.choice(CONFIG["potion_effects"])
            nb_of_turn = self.get_effect_duration(p)
            self.add_effect(effect(self, nb_of_turn))
        else:
            e = random.choice(ennemies)
            self.reporter.log("Choose to Attack {}".format(e.name), self)
            roll = random.randrange(1, 101)
            self.reporter.log("Roll a {}".format(roll), self)
            dmg = 0
            if roll > (100 - self.crit_chance):
                dmg = int(self.atk *  self.crit_power)
                self.reporter.log("CRITICAL Hit {} with {} DMG".format(e.name, dmg), self)
            elif roll >= e.deff:
                dmg = self.atk
                self.reporter.log("Hit {} with {} DMG".format(e.name, dmg), self)
            else:
                self.reporter.log("Missed {}/{}".format(roll, e.deff), self)

            # give DMG
            e.health -= dmg
            if e.health <= 0:
                    self.reporter.log("Dies", e)
    
    def get_effect_duration(self, p):
        rarety = p.get_rarety_name()
        return random.randrange(*CONFIG['effects_duration'][rarety])

    def choose_step(self):
        step = None
        if len(self.potions) != 0:
            if random.random() < CONFIG['potion_chance']:
                step = self.POTION_STEP
            else:
                step = self.ACTION_STEP
        else:
            step = self.ACTION_STEP
        return step

    def add_effect(self, e):
        self.effects.append(e)
        e.start()

    def update_effect(self):
        for e in self.effects:
            e.update()

        finished_effect = filter(lambda e: e.is_finish(), self.effects)
        for e in finished_effect:
            e.stop()
            self.effects.remove(e)
