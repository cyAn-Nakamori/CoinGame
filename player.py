import numpy as np
import random
import math

class player_generator:
    def __init__(self, num: int):
        self.sum = num
        self.policy = [0, 0, 0]
        self.remainder = 0
        self.coinChanges = []
        self.coinChanges.append(num)

    def decision(self):
        self.policy[0] = random.randint(0, self.sum)
        self.policy[1] = random.randint(0, self.sum - self.policy[0])
        self.policy[2] = random.randint(0, self.sum - self.policy[0] - self.policy[1])
        self.remainder = self.sum - self.policy[0] - self.policy[1] - self.policy[2]
        random.shuffle(self.policy)