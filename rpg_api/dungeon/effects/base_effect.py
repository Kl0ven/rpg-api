class Base_Effect(object):
    def __init__(self, user, nb_of_turn):
        self.user = user
        self.nb_of_turn = nb_of_turn
        self.turn = 0 
        self.name = None
        self.reporter = user.reporter
        self.one_shot_effect = False

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def is_finish(self):
        return self.turn > self.nb_of_turn or self.one_shot_effect

    def start(self):
        self.reporter.log("Gained {} effect for {} turns".format(self.name, self.nb_of_turn), self.user)

    def stop(self):
        self.reporter.log("{} effect stopped".format(self.name), self.user)

    def update(self):
        self.turn += 1
        if not self.is_finish():
            self.reporter.log("Has {} {}/{} turns".format(self.name, self.turn, self.nb_of_turn), self.user)
