import random
import time


class Human:
    def __init__(self):
        self.exists = True
        self.energy = 100
        self.healthiness = random.randint(0, 100)
        self.working = False
        self.start_life_loop()

    def start_life_loop(self):
        while self.exists:
            self.study()
            self.sleep()
            self.healthiness -= random.randint(0, 100)
            if self.healthiness <= 0: self.die()

    def study(self):
        while self.energy > random.randint(0, 25):
            try: self.try_something()
            except BlockingIOError: self.improve()

    def sleep(self):
        while self.energy < random.randint(75, 100):
            self.do_nothing()

    def die(self):
        self.exists = False
        self.energy = 0
        self.healthiness = 0

    def do_nothing(self):
        pass

    def try_something(self):
        self.working = True
        time.sleep(random.randint(1, 100))
        self.fail()
        self.working = False

    def fail(self):
        raise BlockingIOError

    def improve(self):
        self.working = True
        time.sleep(random.randint(1, 100))
        self.working = False
