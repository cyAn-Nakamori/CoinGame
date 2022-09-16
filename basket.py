import numpy as np
import random
import math

class Basket:
    # 往篮子中放入硬币分为三种情况：1.双方都不放入硬币  2.仅有一方放入硬币  3.双方都放入硬币
    #   分类后需要对每种情况进行相关定义，包括选择奖励方式(倍率or固定额度)、选择计算对象以及定义奖励倍数or固定额度
    #       1.双方都不放入硬币：
    #           bothNotPutPattern:    0表示采用固定额度方式    *此时双方均不放入硬币，因此仅可采取固定额度方式计算奖励
    #           bothNotPutReward：    定义双方均不放入硬币时获得的固定额度
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
    #       3.双方都放入硬币：
    #           bothSidesCompare：    True表示需要根据放入硬币的多少区分计算奖励
    #                                 False表示不需要根据放入硬币的多少区分计算奖励
    #         若[bothSidesCompare]为False：                   *以下三项参数必填
    #           bothSidesPattern：    0表示采用倍率方式
    #                                 1表示采用固定额度方式
    #           bothSidesObject：     0表示己方放入的硬币数
    #                                 1表示对手放入的硬币数
    #                                 2表示己方+对手放入的硬币数
    #           bothSidesReward：     定义奖励倍数or固定额度
    #         若[bothSidesCompare]为True：                    *以下六项参数选填
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

    def __init__(self, bothNotPutPattern: int, bothNotPutReward: int, putCoinsPattern: int, putCoinsObject: int, putCoinsReward: int, notPutCoinsPattern: int, notPutCoinsObject: int, notPutCoinsReward: int, bothSidesPattern: int, bothSidesObject: int, bothSidesReward: int, bothSidesCompare = False, bigSidePattern = 0, bigSideObject = 0, bigSideReward = 0, smallSidePattern = 0, smallSideObject = 0, smallSideReward = 0):
        #       1.双方都不放入硬币：
        self.bothNotPutPattern = bothNotPutPattern
        self.bothNotPutReward = bothNotPutReward
        #       2.仅有一方放入硬币：
        self.putCoinsPattern = putCoinsPattern
        self.putCoinsObject = putCoinsObject
        self.putCoinsReward = putCoinsReward
        self.notPutCoinsPattern = notPutCoinsPattern
        self.notPutCoinsObject = notPutCoinsObject
        self.notPutCoinsReward = notPutCoinsReward
        #       3.双方都放入硬币：
        self.bothSidesPattern = bothSidesPattern
        self.bothSidesObject = bothSidesObject
        self.bothSidesReward = bothSidesReward
        #       比较硬币多少的标志
        self.bothSidesCompare = bothSidesCompare
        self.bigSidePattern = bigSidePattern
        self.bigSideObject = bigSideObject
        self.bigSideReward = bigSideReward
        self.smallSidePattern = smallSidePattern
        self.smallSideObject = smallSideObject
        self.smallSideReward = smallSideReward

    def both_not_put_calculation(self):
        if self.bothNotPutPattern == 0:
            res = [self.bothNotPutReward, self.bothNotPutReward]
        return res

    def one_side_puts_calculation(self, num_0: int, num_1: int):
        res = [0, 0]
        if self.putCoinsPattern == 0:
            if self.putCoinsObject == 0:
                if num_0:
                    res[0] = num_0 * self.putCoinsReward
                else:
                    res[1] = num_1 * self.putCoinsReward
            elif self.putCoinsObject == 1:
                if num_0:
                    res[0] = num_1 * self.putCoinsReward
                else:
                    res[1] = num_0 * self.putCoinsReward
            elif self.putCoinsObject == 2:
                if num_0:
                    res[0] = (num_0 + num_1) * self.putCoinsReward
                else:
                    res[1] = (num_0 + num_1) * self.putCoinsReward
        elif self.putCoinsPattern == 1:
            if num_0:
                res[0] = self.putCoinsReward
            else:
                res[1] = self.putCoinsReward
        if self.notPutCoinsPattern == 0:
            if self.notPutCoinsObject == 0:
                if num_0 == 0:
                    res[0] = num_0 * self.notPutCoinsReward
                else:
                    res[1] = num_1 * self.notPutCoinsReward
            elif self.notPutCoinsObject == 1:
                if num_0 == 0:
                    res[0] = num_1 * self.notPutCoinsReward
                else:
                    res[1] = num_0 * self.notPutCoinsReward
            elif self.notPutCoinsObject == 2:
                if num_0 == 0:
                    res[0] = (num_0 + num_1) * self.notPutCoinsReward
                else:
                    res[1] = (num_0 + num_1) * self.notPutCoinsReward
        elif self.notPutCoinsPattern == 1:
            if num_0 == 0:
                res[0] = self.notPutCoinsReward
            else:
                res[1] = self.notPutCoinsReward
        return res

    def both_sides_put_calculation(self, num_0: int, num_1:int):
        res = [0, 0]
        if self.bothSidesCompare and num_0 != num_1:
            if self.bigSidePattern == 0:
                if self.bigSideObject == 0:
                    if num_0 > num_1:
                        res[0] = num_0 * self.bigSideReward
                    else:
                        res[1] = num_1 * self.bigSideReward
                elif self.bigSideObject == 1:
                    if num_0 > num_1:
                        res[0] = num_1 * self.bigSideReward
                    else:
                        res[1] = num_0 * self.bigSideReward
                elif self.bigSideObject == 2:
                    if num_0 > num_1:
                        res[0] = (num_0 + num_1) * self.bigSideReward
                    else:
                        res[1] = (num_0 + num_1) * self.bigSideReward
            elif self.bigSidePattern == 1:
                if num_0 > num_1:
                    res[0] = self.bigSideReward
                else:
                    res[1] = self.bigSideReward
            if self.smallSidePattern == 0:
                if self.smallSideObject == 0:
                    if num_0 < num_1:
                        res[0] = num_0 * self.smallSideReward
                    else:
                        res[1] = num_1 * self.smallSideReward
                elif self.smallSideObject == 1:
                    if num_0 < num_1:
                        res[0] = num_1 * self.smallSideReward
                    else:
                        res[1] = num_0 * self.smallSideReward
                elif self.smallSideObject == 2:
                    if num_0 < num_1:
                        res[0] = (num_0 + num_1) * self.smallSideReward
                    else:
                        res[1] = (num_0 + num_1) * self.smallSideReward
            elif self.smallSidePattern == 1:
                if num_0 < num_1:
                    res[0] = self.smallSideReward
                else:
                    res[1] = self.smallSideReward
        else:
            if self.bothSidesPattern == 0:
                if self.bothSidesObject == 0:
                    res[0] = num_0 * self.bothSidesReward
                    res[1] = num_1 * self.bothSidesReward
                elif self.bothSidesObject == 1:
                    res[0] = num_1 * self.bothSidesReward
                    res[1] = num_0 * self.bothSidesReward
                elif self.bothSidesObject == 2:
                    res[0] = (num_0 + num_1) * self.bothSidesReward
                    res[1] = (num_0 + num_1) * self.bothSidesReward
            elif self.bothSidesPattern == 1:
                res[0] = self.bothSidesReward
                res[1] = self.bothSidesReward
        return res

    def calculationResult(self, num_0: int, num_1:int):
        if num_0 != 0 and num_1 != 0:
            res = self.both_sides_put_calculation(num_0, num_1)
        elif num_0 != 0 or num_1 != 0:
            res = self.one_side_puts_calculation(num_0, num_1)
        else:
            res = self.both_not_put_calculation()
        return res