# Camila Richter

import random

class Environment:
    def init(self):
        self.actual_temp = random.randit(0,100) #inicializa la temperatura en un número random

    def get_percept(self):
        return self.actual_temp #devuelve temperatura actual

    def update(self, action):
        if action == "enfriar":
            self.actual_temp -= 1
        elif action == "calentar":
            self.actual_temp += 1
        elif action == "mantener":
            pass

    