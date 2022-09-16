import numpy as np
import random
import math
from player import Player
from basket import Basket
import time
import CoinGame
from CoinGame import RawEnv

# start = time.clock()
coin = 10
coin_for_human = coin
player_1 = Player(coin)
player_2 = Player(coin)

basket_1 = Basket(0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 2, False)
basket_2 = Basket(0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 3, True, 0, 2, 3, 0, 0, 0)
basket_3 = Basket(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, False)

env = RawEnv()
env.startCoins = 10
env.endingFlag["Coins"] = True
env.endingCoins = 100
env.observationModel["GloballyObservable"] = True
env.addBasket(0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 2, False)
env.addBasket(0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 3, True, 0, 2, 3, 0, 0, 0)
env.addBasket(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, False)
env.gameStart()

#
# range_time = 10
# for i in range(range_time):
#     print("——————————现在是第%d局——————————————————\n" % (i + 1))
#     print("Player_1持有的硬币数为：%d\n" % player_1.sum)
#     print("Player_2持有的硬币数为：%d\n" % player_2.sum)
#     print("-----游戏开始！请双方给出游戏决策-----\n")
#     player_1.decision()
#     policy_1 = player_1.policy
#     player_2.decision()
#     policy_2 = player_2.policy
#     print("Player_1给出的游戏决策为%d  %d  %d  余%d枚\n" % (policy_1[0], policy_1[1], policy_1[2], player_1.remainder))
#     print("Player_2给出的游戏决策为%d  %d  %d  余%d枚\n" % (policy_2[0], policy_2[1], policy_2[2], player_2.remainder))
#     res = basket_1.calculationResult(policy_1[0], policy_2[0])
#     print("     第一个筐的计算结果为%d\n                      %d\n" % (res[0], res[1]))
#     player_1.remainder += res[0]
#     player_2.remainder += res[1]
#     # print("&&&&&&&  %d     %d  &&&&&&&\n" % (res[0], res[1]))
#     res = basket_2.calculationResult(policy_1[1], policy_2[1])
#     print("     第二个筐的计算结果为%d\n                      %d\n" % (res[0], res[1]))
#     player_1.remainder += res[0]
#     player_2.remainder += res[1]
#     # print("&&&&&&&  %d     %d  &&&&&&&\n" % (res[0], res[1]))
#     res = basket_3.calculationResult(policy_1[2], policy_2[2])
#     print("     第三个筐的计算结果为%d\n                      %d\n" % (res[0], res[1]))
#     player_1.remainder += res[0]
#     player_2.remainder += res[1]
#     # print("&&&&&&&  %d     %d  &&&&&&&\n" % (res[0], res[1]))
#     print("————————————————游戏结果为————————————————\n")
#     print("Player_1持有的硬币数为：%d\n" % player_1.remainder)
#     print("Player_2持有的硬币数为：%d\n" % player_2.remainder)
#     if player_1.remainder == 0:
#         print("+++++游戏结束！Player_2获胜！+++++")
#         break
#     elif player_2.remainder == 0:
#         print("+++++游戏结束！Player_1获胜！+++++")
#         break
#     player_1.sum = player_1.remainder
#     player_1.remainder = 0
#     player_2.sum = player_2.remainder
#     player_2.remainder = 0
#     player_1.coinChanges.append(player_1.sum)
#     player_2.coinChanges.append(player_2.sum)

