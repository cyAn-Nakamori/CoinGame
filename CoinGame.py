import numpy as np
from gym import spaces
import basket

def env():
    env = raw_env()
    # 设置默认初始状态：双方各持有10枚硬币
    #                游戏结束标志为先持有100枚及以上硬币的玩家获胜
    #                观测模式为GloballyObservable
    env.startCoins = 10
    env.endingFlag["coins"] = True
    env.endingCoins = 100
    env.observation_model["GloballyObservable"] = True
    return env

class raw_env():
    def __init__(self):
        self.startCoins = 0
        self.agents = ["player_1", "player_2"]
        self.endingFlag = {"coins": False, "rounds": False}
        self.endingCoins = 0
        self.endingRounds = 0
        # 观测模式：
        #        无论是哪种观测模式，玩家均可观测到自己放置于每个框内的硬币数以及游戏结果
        #        GloballyObservable：玩家可观测到对手放置于每个框内的硬币数以及对手手中持有的硬币数
        #        PartiallyObservable：玩家仅可观测到对手放置于每个框内的硬币数，无法观测到对手手中持有的硬币数
        #        Unobservable：玩家无法观测到对手放置于每个框内的硬币数以及对手手中持有的硬币数
        self.observation_model = {"GloballyObservable": False, "PartiallyObservable": False, "Unobservable": False}
        self.rewards = {i: 0 for i in self.agents}
        self.dones = {i: False for i in self.agents}
        self.baskets = []

    def addBasket(self):


    def step(self, action):


    def observe(self, agent):