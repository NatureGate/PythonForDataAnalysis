# -*- coding: UTF-8 -*-
#### 4.6伪随机数的生成
import numpy as np

arr = np.random.normal(size=(4,4))
print(arr)

###修改随机数种子
np.random.seed(110)
## numpy.random中部分函数列表
##seed                   向随机数生成器传递随机状态种子
##permutation            返回一个序列的随机序列,或者返回一个乱序的证书范围序列
##shuffle                随机排列一个序列
##rand                   从均匀分布中抽取样本
##randint                从给定的由低到高的范围抽取随机整数
##randn                  从均值为0方差为1的正态分布中抽取样本
##binomial               从二项分布中抽取样本
##normal                 从正态分布中抽取样本呢
##beta                   从beta分布中抽取样本
##chisquare              从卡方分布中抽取样本
##gama                   从gama分布中抽取样本
##uniform                从(0,1)分布中抽取样本