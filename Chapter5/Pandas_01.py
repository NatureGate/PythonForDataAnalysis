# -*- coding: UTF-8 -*-
import  pandas as pd
import  numpy as np
from pandas import  Series,DataFrame
###  Series是一个既包含数组,也包含dict的结构
##   既可以随机访问,也可以通过hash访问
obj = pd.Series([2,4,6,1,-3])
print(obj)
print(obj.values)
print(obj.index)
obj2 = Series([1,2,3,4,],index=['a','b','c','d'] )
print('get a = '+str(obj2['a']))
print(obj2[['a','b','c']])
print(obj2>3)
print(obj2*3)
print(np.exp(obj2))

