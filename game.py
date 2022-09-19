import numpy as np
import random
import math
from player import Player
from basket import BasketGenerator
import time
import CoinGame
from CoinGame import RawEnv

def rule_1(input_1, input_2):
    output_1, output_2 = 0, 0
    if input_1 > 0 and input_2 > 0:
        output_1 = 2 * input_1
        output_2 = 2 * input_2
    elif input_1 != 0 and input_2 == 0:
        output_2 = 2 * input_1
    elif input_1 == 0 and input_2 != 0:
        output_1 = 2 * input_2
    return [output_1, output_2]

def rule_2(input_1 = 0, input_2 = 0):
    output_1, output_2 = 0, 0
    if input_1 > 0 and input_2 > 0:
        if input_1 > input_2:
            output_1 = 3 * (input_1 + input_2)
        elif input_1 < input_2:
            output_2 = 3 * (input_1 + input_2)
        else:
            output_1 = 3 * (input_1 + input_2)
            output_2 = 3 * (input_1 + input_2)
    elif input_1 != 0 and input_2 == 0:
        output_2 = 2 * input_1
    elif input_1 == 0 and input_2 != 0:
        output_1 = 2 * input_2
    return [output_1, output_2]

def rule_3(input_1 = 0, input_2 = 0):
    output_1, output_2 = 0, 0
    if input_1 > 0 and input_2 > 0:
        output_1 = 2 * input_1
        output_2 = 2 * input_2
    return [output_1, output_2]

if __name__== "__main__" :

    # start = time.clock()
    # coin = 10
    # coin_for_human = coin
    # player_1 = Player(coin)
    # player_2 = Player(coin)

    env = RawEnv()
    env.model["human vs machine"] = True
    env.startCoins = 10
    env.endingFlag["Coins"] = True
    env.endingCoins = 500
    env.endingRounds = 20
    # env.observationModel["GloballyObservable"] = True
    basket_1 = BasketGenerator()
    basket_2 = BasketGenerator()
    basket_3 = BasketGenerator()
    basket_1.setRule(rule_1)
    basket_2.setRule(rule_2)
    basket_3.setRule(rule_3)
    env.addBasket(basket_1)
    env.addBasket(basket_2)
    env.addBasket(basket_3)

    env.gameStart()



