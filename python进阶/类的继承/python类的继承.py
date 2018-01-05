# !user/bin/python
class Anminal(object):
    def __init__(self, eat, run):
        self.eat = eat
        self.run = run


class Dog(Anminal):
    def __init__(self, eat, run, sleep, jump):
        super(Anminal.__init__(eat, run))
        self.sleep = sleep
        self.jump = jump


d1 = Dog('eat bones', 'run away', 'sleep night', 'jump away')

print(d1.eat)
