import numpy as np
from gym import spaces
import basket
import player
from basket import BasketGenerator
from player import Player

class RawEnv():
    def __init__(self):
        self.startCoins = 0
        self.model = {"machine vs machine": False, "human vs machine": False}
        self.agents = []
        self.endingFlag = {"Coins": False, "Rounds": False}
        self.endingCoins = 0
        self.endingRounds = 0
        self.currentRound = 1
        # 观测模式：
        #        无论是哪种观测模式，玩家均可观测到自己放置于每个框内的硬币数以及游戏结果
        #        GloballyObservable：玩家可观测到对手放置于每个框内的硬币数以及对手手中持有的硬币数
        #        PartiallyObservable：玩家仅可观测到对手放置于每个框内的硬币数，无法观测到对手手中持有的硬币数
        #        Unobservable：玩家无法观测到对手放置于每个框内的硬币数以及对手手中持有的硬币数
        self.observationModel = {"GloballyObservable": False, "PartiallyObservable": False, "Unobservable": False}
        self.rewards = {i: 0 for i in self.agents}
        self.dones = [False, False]
        self.baskets = []

    def addBasket(self, basket: BasketGenerator):
        self.baskets.append(basket)

    # 每个回合的操作
    def step(self, action):
        res_1, res_2, res = [], [], []
        # basket = BasketGenerator()
        for i in range(len(self.baskets)):
            print("********** 第 %d 个筐 **********\n" % (i + 1))
            basket = self.baskets[i]
            print("Player_1放入的硬币数为 %d , Player_2放入的硬币数为 %d \n" %(action[0][i], action[1][i]))
            cal = basket.basketCalculation(action[0][i], action[1][i])
            print("结果：Player_1获得 %d 枚硬币，Player_2获得 %d 枚硬币\n" %(cal[0], cal[1]))
            res_1.append(cal[0])
            res_2.append(cal[1])
        res.append(res_1)
        res.append(res_2)
        return res

    # def observe(self, agent):

    # 持有硬币为0不是终止游戏的条件
    def judgment(self):
        if self.endingFlag["Coins"] == True:
            if self.agents[0].sum >= self.endingCoins and self.agents[0].sum > self.agents[1].sum:
                self.dones[0] = True
                return True
            elif self.agents[1].sum >= self.endingCoins and self.agents[0].sum < self.agents[1].sum:
                self.dones[1] = True
                return True
            elif self.agents[0].sum == self.agents[1].sum and self.agents[0].sum >= self.endingCoins:
                self.dones = [True, True]
                return True
        elif self.endingFlag["Rounds"] == True:
            if self.agents[0].sum >self.agents[1].sum:
                self.dones = [True, False]
                return True
            elif self.agents[0].sum < self.agents[1].sum:
                self.dones = [False, True]
                return True
            else:
                self.dones = [True, True]
                return True
        else:
            return False

    def printResult(self):
        if self.model["machine vs machine"]:
            if self.dones[0] and self.dones[1]:
                print("-------------------平局！--------------------\n")
            elif self.dones[0]:
                print("----------------Player_1获胜！---------------\n")
            elif self.dones[1]:
                print("----------------Player_2获胜！---------------\n")
            else:
                print("-----------------没有获胜选手-----------------\n")
        elif self.model["human vs machine"]:
            if self.dones[0] and self.dones[1]:
                print("-------------------平局！--------------------\n")
            elif self.dones[0]:
                print("----------------人类玩家获胜！---------------\n")
            elif self.dones[1]:
                print("-----------------机器人获胜！---------------\n")
            else:
                print("-----------------没有获胜选手-----------------\n")

    def gameStart(self):
        player_1 = Player(self.startCoins)
        player_2 = Player(self.startCoins)
        self.agents.append(player_1)
        self.agents.append(player_2)
        print("-------------------游戏开始-------------------\n")
        if self.model["machine vs machine"]:
            if self.endingFlag["Coins"] == True:
                while 1:
                    print("-----------------第 %d 局-----------------\n" % self.currentRound)
                    self.currentRound += 1
                    print("@@@@@  Player_1持有硬币 %d 枚, Player_2持有硬币 %d 枚  @@@@@\n" % (player_1.sum, player_2.sum))
                    player_1.decision(self.baskets)
                    player_2.decision(self.baskets)
                    print("----------Player_1决策为", end="")
                    for i in player_1.policy:
                        print(" %d" % i, end="")
                    print("----------\n")
                    print("----------Player_2决策为", end="")
                    for i in player_2.policy:
                        print(" %d" % i, end="")
                    print("----------\n")
                    action = [player_1.policy, player_2.policy]
                    res = self.step(action)
                    print("--------本局硬币放置情况为", end="")
                    for i in res[0]:
                        print(" %d" % i, end="")
                    print("----------\n")
                    print("-----------------------", end="")
                    for i in res[1]:
                        print(" %d" % i, end="")
                    print("----------\n")
                    player_1.coinChange(res[0])
                    player_2.coinChange(res[1])
                    print("@@@@@  Player_1持有硬币 %d 枚, Player_2持有硬币 %d 枚  @@@@@\n" % (player_1.sum, player_2.sum))
                    if self.judgment():
                        self.currentRound -= 1
                        break
            elif self.endingFlag["Rounds"] == True:
                while self.currentRound <= self.endingRounds:
                    print("-----------------第 %d 局-----------------\n" % self.currentRound)
                    self.currentRound += 1
                    player_1.decision(self.baskets)
                    player_2.decision(self.baskets)
                    print("----------Player_1决策为", end="")
                    for i in player_1.policy:
                        print(" %d" % i, end="")
                    print("----------\n", end="")
                    print("----------Player_2决策为", end="")
                    for i in player_2.policy:
                        print(" %d" % i, end="")
                    print("----------\n")
                    action = [player_1.policy, player_2.policy]
                    res = self.step(action)
                    print("--------本局硬币放置情况为", end="")
                    for i in res[0]:
                        print(" %d" % i, end="")
                    print("----------\n")
                    print("-----------------------", end="")
                    for i in res[1]:
                        print(" %d" % i, end="")
                    print("----------\n")
                    player_1.coinChange(res[0])
                    player_2.coinChange(res[1])
                print("@@@@@  Player_1持有硬币 %d 枚, Player_2持有硬币 %d 枚  @@@@@\n" % (player_1.sum, player_2.sum))
                self.judgment()
                self.currentRound -= 1
        elif self.model["human vs machine"]:
            if self.endingFlag["Coins"] == True:
                while 1:
                    print("-----------------第 %d 局-----------------\n" % self.currentRound)
                    self.currentRound += 1
                    print("@@@@@  人类玩家持有硬币 %d 枚, 机器人持有硬币 %d 枚  @@@@@\n" % (player_1.sum, player_2.sum))
                    # 人类玩家输入
                    print("请输入在每个筐中放入的硬币数：", end="")
                    player_1.policy = list(map(int,input().split()))
                    player_2.decision(self.baskets)
                    print("----------人类玩家决策为", end="")
                    for i in player_1.policy:
                        print(" %d" % i, end="")
                    print("----------\n")
                    print("----------机器人决策为", end="")
                    for i in player_2.policy:
                        print(" %d" % i, end="")
                    print("----------\n")
                    action = [player_1.policy, player_2.policy]
                    res = self.step(action)
                    print("--------本局硬币放置情况为", end="")
                    for i in res[0]:
                        print(" %d" % i, end="")
                    print("----------\n")
                    print("-----------------------", end="")
                    for i in res[1]:
                        print(" %d" % i, end="")
                    print("----------\n")
                    player_1.coinChange(res[0])
                    player_2.coinChange(res[1])
                    print("@@@@@  人类玩家持有硬币 %d 枚, 机器人持有硬币 %d 枚  @@@@@\n" % (player_1.sum, player_2.sum))
                    if self.judgment():
                        self.currentRound -= 1
                        break
            elif self.endingFlag["Rounds"] == True:
                while self.currentRound <= self.endingRounds:
                    print("-----------------第 %d 局-----------------\n" % self.currentRound)
                    self.currentRound += 1
                    # 人类玩家输入
                    print("请输入在每个筐中放入的硬币数：", end="")
                    player_1.policy = list(map(int, input().split()))
                    player_2.decision(self.baskets)
                    print("----------人类玩家决策为", end="")
                    for i in player_1.policy:
                        print(" %d" % i, end="")
                    print("----------\n", end="")
                    print("----------机器人决策为", end="")
                    for i in player_2.policy:
                        print(" %d" % i, end="")
                    print("----------\n")
                    action = [player_1.policy, player_2.policy]
                    res = self.step(action)
                    print("--------本局硬币放置情况为", end="")
                    for i in res[0]:
                        print(" %d" % i, end="")
                    print("----------\n")
                    print("-----------------------", end="")
                    for i in res[1]:
                        print(" %d" % i, end="")
                    print("----------\n")
                    player_1.coinChange(res[0])
                    player_2.coinChange(res[1])
                    print("@@@@@  人类玩家持有硬币 %d 枚, 机器人持有硬币 %d 枚  @@@@@\n" % (player_1.sum, player_2.sum))
                self.judgment()
                self.currentRound -= 1
        self.printResult()