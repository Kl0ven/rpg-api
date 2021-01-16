from config import CONFIG
import random 

class Character(object):
    POTION_STEP=0
    ACTION_STEP=1

    def __init__(self, name, rep, atk=2, deff=2, health=CONFIG["max_health"], potions=[]):
        self.atk = atk
        self.deff = deff
        self.potions = potions
        self.health = health
        self.initiative = None
        self.reporter = rep
        self.name = name
        self.crit_chance = CONFIG['crit']
        self.crit_power = CONFIG['crit_power']
        self.effects = []

    def __str__(self):
        return "{}(health: {}, atk: {}, def: {})".format(self.name, self.health, self.atk, self.deff)

    def __repr__(self):
        return str(self)

    def roll_initiative(self):
        self.initiative = random.randrange(1, 101)

    def is_alive(self):
        return self.health > 0

    def turn(self, ennemy):
        self.update_effect()
        step = self.choose_step()
        if step == self.POTION_STEP:
            p = random.choice(self.potions)
            p.used = True
            self.reporter.log("Choose to use a {}".format(p.name), self)
            effect = random.choice(CONFIG["potion_effects"])
            nb_of_turn = 2
            self.add_effect(effect(self, nb_of_turn))
        else:
            pass

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
