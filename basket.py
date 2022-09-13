import numpy as np
import random
import math

class basket_generator:

    # 往篮子中放入硬币分为三种情况：1.双方都放入硬币  2.仅有一方放入硬币  3.双方都不放入硬币
    #   分类后需要对每种情况进行相关定义，包括选择奖励方式(倍率or固定额度)、选择计算对象以及定义奖励倍数or固定额度
    #       1.双方都放入硬币：
    #           bothSidesCompare：    True表示需要根据放入硬币的多少区分计算奖励
    #                                 False表示不需要根据放入硬币的多少区分计算奖励
    #         若[bothSidesCompare]为False：
    #           bothSidesPattern：    0表示采用倍率方式
    #                                 1表示采用固定额度方式
    #           bothSidesObject：     0表示己方放入的硬币数
    #                                 1表示对手放入的硬币数
    #                                 2表示己方+对手放入的硬币数
    #           bothSidesReward：     定义奖励倍数or固定额度
    #         若[bothSidesCompare]为True：
    #           bigSidePattern：      0表示采用倍率方式
    #                                 1表示采用固定额度方式
    #           bigSideObject：       0表示己方放入的硬币数
    #                                 1表示对手放入的硬币数
    #                                 2表示己方+对手放入的硬币数
    #           bigSideReward：       定义放入硬币数多者获得的奖励倍数or固定额度
    #           smallSidePattern：    0表示采用倍率方式
    #                                 1表示采用固定额度方式
    #           smallSideObject：     0表示己方放入的硬币数
    #                                 1表示对手放入的硬币数
    #                                 2表示己方+对手放入的硬币数
    #           smallSideReward：     定义放入硬币数少者获得的奖励倍数or固定额度
    #       2.仅有一方放入硬币：
    #           putCoinsPattern：     0表示采用倍率方式
    #                                 1表示采用固定额度方式
    #           putCoinsObject：      0表示己方放入的硬币数
    #                                 1表示对手放入的硬币数
    #                                 2表示己方+对手放入的硬币数
    #           putCoinsReward：      定义放入硬币者获得的奖励倍数or固定额度
    #           notPutCoinsPattern：  0表示采用倍率方式
    #                                 1表示采用固定额度方式
    #           notPutCoinsObject：   0表示己方放入的硬币数
    #                                 1表示对手放入的硬币数
    #                                 2表示己方+对手放入的硬币数
    #           notPutCoinsReward：   定义不放入硬币者获得的奖励倍数or固定额度
    #       3.双方都不放入硬币：
    #           bothNotPutPattern:    0表示采用固定额度方式    *此时双方均不放入硬币，因此仅可采取固定额度方式计算奖励
    #           bothNotPutReward：    定义双方均不放入硬币时获得的固定额度

    def __init__(self, bothSidesRate: int, ifCompare: bool, biggerNumberRate: int, smallerNumberRate: int, oneSideForPutRate: int,oneSideForNotPutRate: int,noneSideAddition: int):
        self.bothSidesRate = bothSidesRate
        self.ifCompare = ifCompare
        self.biggerNumberRate = biggerNumberRate
        self.smallerNumberRate = smallerNumberRate
        self.oneSideForPutRate = oneSideForPutRate
        self.oneSideForNotPutRate = oneSideForNotPutRate
        self.noneSideAddition = noneSideAddition

    def calculateForBothSides(self, num_0: int, num_1:int):
        res = [num_0, num_1]
        if self.ifCompare:
            if num_0 > num_1:
                res[0] = (num_0 + num_1) * self.biggerNumberRate
                res[1] *= self.smallerNumberRate
            elif num_0 < num_1:
                res[0] *= self.smallerNumberRate
                res[1] = (num_0 + num_1) * self.biggerNumberRate
            else:
                res[0] *= self.bothSidesRate
                res[1] *= self.bothSidesRate
        else:
            res[0] *= self.bothSidesRate
            res[1] *= self.bothSidesRate
        return res

    def calculateForOneSide(self, num_0: int, num_1: int):
        res = [num_0, num_1]
        if num_0:
            res[0] = num_0 * self.oneSideForPutRate
            res[1] = num_0 * self.oneSideForNotPutRate
        else:
            res[0] = num_1 * self.oneSideForNotPutRate
            res[1] = num_1 * self.oneSideForPutRate
        return res

    def calculateForNoneSide(self):
        res = [self.noneSideAddition, self.noneSideAddition]
        return res

    def calculationResult(self, num_0: int, num_1:int):
        if num_0 != 0 and num_1 != 0:
            res = self.calculateForBothSides(num_0, num_1)
        elif num_0 != 0 or num_1 != 0:
            res = self.calculateForOneSide(num_0, num_1)
        else:
            res = self.calculateForNoneSide()
        return res