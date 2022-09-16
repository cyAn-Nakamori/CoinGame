import numpy as np
from gym import spaces
import basket
import player
from basket import Basket
from player import Player

# def env():
#     env = RawEnv()
#     # 设置默认初始状态：双方各持有10枚硬币
#     #                游戏结束标志为先持有100枚及以上硬币的玩家获胜
#     #                观测模式为GloballyObservable
#     env.startCoins = 10
#     env.endingFlag["Coins"] = True
#     env.endingCoins = 100
#     env.observationModel["GloballyObservable"] = True
#     return env

class RawEnv():
    def __init__(self):
        self.startCoins = 0
        self.agents = ["Player_1", "Player_2"]
        self.endingFlag = {"Coins": False, "Rounds": False}
        self.endingCoins = 0
        self.endingRounds = 0
        # 观测模式：
        #        无论是哪种观测模式，玩家均可观测到自己放置于每个框内的硬币数以及游戏结果
        #        GloballyObservable：玩家可观测到对手放置于每个框内的硬币数以及对手手中持有的硬币数
        #        PartiallyObservable：玩家仅可观测到对手放置于每个框内的硬币数，无法观测到对手手中持有的硬币数
        #        Unobservable：玩家无法观测到对手放置于每个框内的硬币数以及对手手中持有的硬币数
        self.observationModel = {"GloballyObservable": False, "PartiallyObservable": False, "Unobservable": False}
        self.rewards = {i: 0 for i in self.agents}
        self.dones = [False, False]
        self.baskets = []

    def addBasket(self, bothNotPutPattern: int, bothNotPutReward: int, putCoinsPattern: int, putCoinsObject: int, putCoinsReward: int, notPutCoinsPattern: int, notPutCoinsObject: int, notPutCoinsReward: int, bothSidesPattern: int, bothSidesObject: int, bothSidesReward: int, bothSidesCompare = False, bigSidePattern = 0, bigSideObject = 0, bigSideReward = 0, smallSidePattern = 0, smallSideObject = 0, smallSideReward = 0):
        basket = Basket(bothNotPutPattern, bothNotPutReward, putCoinsPattern, putCoinsObject, putCoinsReward, notPutCoinsPattern, notPutCoinsObject, notPutCoinsReward, bothSidesPattern, bothSidesObject, bothSidesReward, bothSidesCompare, bigSidePattern, bigSideObject, bigSideReward, smallSidePattern, smallSideObject, smallSideReward)
        self.baskets.append(basket)

    # 每个回合的操作
    def step(self, action):
        res_1, res_2, res = [], [], []
        # basket = BasketGenerator()
        for i in range(len(self.baskets)):
            basket = self.baskets[i]
            print("当前篮子参数为 %d %d %d %d %d %d %d %d %d %d %d %s %d %d %d %d %d %d\n" %(basket.bothNotPutPattern, basket.bothNotPutReward, basket.putCoinsPattern, basket.putCoinsObject, basket.putCoinsReward, basket.notPutCoinsPattern, basket.notPutCoinsObject, basket.notPutCoinsReward, basket.bothSidesPattern, basket.bothSidesObject, basket.bothSidesReward, basket.bothSidesCompare, basket.bigSidePattern, basket.bigSideObject, basket.bigSideReward, basket.smallSidePattern, basket.smallSideObject, basket.smallSideReward))
            print("Player_1放入的硬币数为 %d , Player_2放入的硬币数为 %d \n" %(action[0][i], action[1][i]))
            res = basket.calculationResult(action[0][i], action[1][i])
            print("本局结果：Player_1获得 %d 枚硬币，Player_2获得 %d 枚硬币\n" %(res[0], res[1]))
            res_1.append(res[0])
            res_2.append(res[1])
        res.append([res_1, res_2])
        return res

    # def observe(self, agent):

    def gameStart(self):
        player_1 = Player(self.startCoins)
        player_2 = Player(self.startCoins)
        print("-------------------游戏开始-------------------\n")
        if self.endingFlag["Coins"] == True:
            while self.dones[0] == False and self.dones[1] == False:
                count = 0
                print("-----------------第 %d 局-----------------\n" % count)
                count += 1
                player_1.decision(self.baskets)
                player_2.decision(self.baskets)
                print("----------Player_1决策为")
                for i in player_1.policy:
                    print(" %d" % i)
                print("----------\n")
                print("----------Player_2决策为")
                for i in player_2.policy:
                    print(" %d" % i)
                print("----------\n")
                action = [player_1.policy, player_2.policy]
                res = self.step(action)
                print("---------------计算结果为")
                for i in res[0]:
                    print(" %d" % i)
                print("----------\n")
                print("-----------------------")
                for i in res[1]:
                    print(" %d" % i)
                print("----------\n")
                player_1.coinChanges(res[0])
                player_2.coinChanges(res[1])
                if player_1.sum >= self.endingCoins and player_1.sum > player_2.sum:
                    self.dones[0] = True
                elif player_2.sum >= self.endingCoins and player_1.sum < player_2.sum:
                    self.dones[1] = True
                elif player_1.sum == player_2.sum and player_1.sum >= self.endingCoins:
                    self.dones = [True, True]
        elif self.endingFlag["Rounds"] == True:
            roundCounter = 0
            while roundCounter <= self.endingRounds:
                roundCounter += 1
                print("-----------------第 %d 局-----------------\n" % roundCounter)
                player_1.decision(self.baskets)
                player_2.decision(self.baskets)
                print("----------Player_1决策为")
                for i in player_1.policy:
                    print(" %d" % i)
                print("----------\n")
                print("----------Player_2决策为")
                for i in player_2.policy:
                    print(" %d" % i)
                print("----------\n")
                action = [player_1.policy, player_2.policy]
                res = self.step(action)
                print("---------------计算结果为")
                for i in res[0]:
                    print(" %d" % i)
                print("----------\n")
                print("-----------------------")
                for i in res[1]:
                    print(" %d" % i)
                print("----------\n")
                player_1.coinChanges(res[0])
                player_2.coinChanges(res[1])
            self.dones = [True, False] if player_1.sum > player_2.sum else [False, True]
        if self.dones[0] and self.dones[1]:
            print("-------------------平局！--------------------\n")
        elif self.dones[0]:
            print("----------------Player_1获胜！---------------\n")
        elif self.dones[1]:
            print("----------------Player_2获胜！---------------\n")
        else:
            print("------------------没有获胜选手----------------\n")