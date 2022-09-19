import numpy as np
import random
import math

class BasketGenerator:

    def __init__(self):
        self.rule = None

    # 定义抽象类函数，限定输入和输出，由用户定义篮子的规则
    def basketRule(self, input_1: int, input_2: int):
        pass

    def setRule(self, rule):
        self.rule = rule

    def basketCalculation(self, input_1: int, input_2: int):
        return self.rule(input_1, input_2)
