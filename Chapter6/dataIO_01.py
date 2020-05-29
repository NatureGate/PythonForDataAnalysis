# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

df = pd.read_csv('ex1.csv')
print(df)
df2 = pd.read_table('ex1.csv', sep=",", header=None)
print(df2)
df3 = pd.read_table('ex1.csv', sep=",", names=['a', 'b', 'c', 'd', 'message'])
print(df3)
names = ['a', 'b', 'c', 'd', 'message']
df4 = pd.read_csv('ex1.csv', names=names, index_col='message')
print(df4)

###多列分层索引
parsed = pd.read_csv('ex2.csv',index_col=['key1','key2'])
print(parsed)

######跳过某些行 skiprows
df4 = pd.read_csv('ex4.csv',skiprows=[0,2,3])
print(df4)
###
print(pd.read_csv('ex5.csv'))
print(pd.read_csv('ex5.csv',na_values=['NULL']))
##在字典中,每列可以指定不同的缺失值标识
sentinels = {'message':['foo','NA'],'something':['two']}
print(pd.read_csv('ex5.csv',na_values=sentinels))

###分块读入文本文件#nrows用来指明行数


























