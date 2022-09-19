import numpy as np
import random
import math
import basket
from basket import BasketGenerator

class Player:
    def __init__(self, num: int):
        self.model = {"human": False, "machine": False}
        self.sum = num
        self.policy = []
        self.remainder = 0
        self.coinSumChange = []
        self.coinSumChange.append(num)

    def decision(self, baskets):
        self.remainder = self.sum
        self.policy = []
        for i in range(len(baskets)):
            basket = baskets[i]
            if self.remainder:
                self.policy.append(random.randint(0, self.remainder))
            else:
                self.policy.append(0)
            self.remainder -= self.policy[i]
        random.shuffle(self.policy)

    def coinChange(self, res: list):
        self.sum = self.remainder
        for i in res:
            self.sum += i