import numpy as np
import random
import math
import basket
from basket import Basket

class Player:
    def __init__(self, num: int):
        self.model = {"human": False, "machine": False}
        self.sum = num
        self.policy = [0, 0, 0]
        self.remainder = 0
        self.coinChanges = []
        self.coinChanges.append(num)

    def decision(self, baskets):
        self.remainder = self.sum
        for i in range(len(baskets)):
            basket = baskets[i]
            self.policy.append(random.randint(0, self.remainder))
            self.remainder -= self.policy[i]
        random.shuffle(self.policy)

    def coinChange(self, res):
        self.sum = self.remainder
        for i in res:
            self.sum += i