import numpy as np
import random
import math
from player import player_generator
from basket import basket_generator
import time
import CoinGame

start = time.clock()
coin = 10
coin_for_human = coin
player_1 = player_generator(coin)
player_2 = player_generator(coin)

basket_1 = basket_generator(2, False, 0, 0, 0, 2, 0)
basket_2 = basket_generator(3, True, 3, 0, 0, 2, 0)
basket_3 = basket_generator(2, False, 0, 0, 0, 0, 0)
# def basket_1(num1: int, num2: int):
#     if num1 != 0 and num2 != 0:
#         num1 <<= 1
#         num2 <<= 1
#     elif num1 != 0 and num2 == 0:
#         num2 = num1 << 1
#         num1 = 0
#     elif num1 == 0 and num2 != 0:
#         num1 = num2 << 1
#         num2 = 1
#     res = [num1, num2]
#     return res

# def basket_2(num1: int, num2: int):
#     if num1 != 0 and num2 != 0:
#         if num1 > num2:
#             num2 = (num1 + num2) * 3
#             num1 = 0
#         elif num1 < num2:
#             num1 = (num1 + num2) * 3
#             num2 = 0
#         else:
#             num1 *= 3
#             num2 *= 3
#     elif num1 != 0 and num2 == 0:
#         num2 = num1 << 1
#         num1 = 0
#     elif num1 == 0 and num2 != 0:
#         num1 = num2 << 1
#         num2 = 1
#     res = [num1, num2]
#     return res

# def basket_3(num1: int, num2: int):
#     if num1 != 0 and num2 != 0:
#         num1 <<= 1
#         num2 <<= 1
#     else:
#         num1 = 0
#         num2 = 0
#     res = [num1, num2]
#     return res

range_time = 10
for i in range(range_time):
    print("——————————现在是第%d局——————————————————\n" % i)
    print("Player_1持有的硬币数为：%d\n" % player_1.sum)
    print("Player_2持有的硬币数为：%d\n" % player_2.sum)
    print("-----游戏开始！请双方给出游戏决策-----\n")
    player_1.decision()
    policy_1 = player_1.policy
    player_2.decision()
    policy_2 = player_2.policy
    print("Player_1给出的游戏决策为%d  %d  %d  余%d枚\n" % (policy_1[0], policy_1[1], policy_1[2], player_1.remainder))
    print("Player_2给出的游戏决策为%d  %d  %d  余%d枚\n" % (policy_2[0], policy_2[1], policy_2[2], player_2.remainder))
    res = basket_1.calculationResult(policy_1[0], policy_2[0])
    player_1.remainder += res[0]
    player_2.remainder += res[1]
    # print("&&&&&&&  %d     %d  &&&&&&&\n" % (res[0], res[1]))
    res = basket_2.calculationResult(policy_1[1], policy_2[1])
    player_1.remainder += res[0]
    player_2.remainder += res[1]
    # print("&&&&&&&  %d     %d  &&&&&&&\n" % (res[0], res[1]))
    res = basket_3.calculationResult(policy_1[2], policy_2[2])
    player_1.remainder += res[0]
    player_2.remainder += res[1]
    # print("&&&&&&&  %d     %d  &&&&&&&\n" % (res[0], res[1]))
    print("————————————————游戏结果为————————————————\n")
    print("Player_1持有的硬币数为：%d\n" % player_1.remainder)
    print("Player_2持有的硬币数为：%d\n" % player_2.remainder)
    if player_1.remainder == 0:
        print("+++++游戏结束！Player_2获胜！+++++")
        break
    elif player_2.remainder == 0:
        print("+++++游戏结束！Player_1获胜！+++++")
        break
    player_1.sum = player_1.remainder
    player_1.remainder = 0
    player_2.sum = player_2.remainder
    player_2.remainder = 0
    player_1.coinChanges.append(player_1.sum)
    player_2.coinChanges.append(player_2.sum)

env = CoinGame.env()
env.startCoins = 10

test = basket_generator(2, False, 0, 0, 0, 2, 0)
test.bothSidesRate = 2
