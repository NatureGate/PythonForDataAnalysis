# -*- coding: UTF-8 -*-
###描述性统计的概述与计算

import pandas as pd
import numpy as np

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])
##sum方法默认axis = 0
print(df.sum())
###最大值的索引值,one最大值为7.1,索引为b,two的最大值为-1.3,索引是d
print(df.idxmax())
print(df.describe())
##count 非NA值的个数
print(df.count())
## min,max 分别计算最小值,最大值
print(df.max())

##mean 均值
print(df.mean())

## median 中位数
print(df.median())

## mad 平均值的平均绝对偏差
print(df.mad())

###########    相关性和协方差

