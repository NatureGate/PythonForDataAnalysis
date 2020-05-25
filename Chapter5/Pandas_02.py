# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np

####重建索引
## @param
# index:新建索引的序列,可以是索引实例或任意其他序列型Python数据结构,索引使用时无需复制
# method:插值方式,'ffill'为向前填充,而'bfill'是向后填充
# fill_value:缺失插入的默认值
# limit:向后或向前填充时,所需填充的最大尺寸间隙
# tolerance:
# level: 匹配MultiIndex级别的简单索引,否则选择子集
# copy: 如果为true,即使新索引等于旧索引,也总是复制底层数据;如果为false,则在索引相同时不需要复制数据
obj = pd.Series(range(4), index=['a', 'b', 'c', 'd'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj)
print(obj2)

###索引填充
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
obj4 = obj3.reindex(range(6), method='ffill')
print(obj4)

###利用frame重建索引
frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
print(frame)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)

####轴向上删除条目
obj = pd.Series(range(5), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
new_obj = obj.drop('c')
print(obj)
print(obj.drop(['d', 'e']))

##从轴上删除索引值,默认轴为0 ,inplace 默认为false
data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
data.drop(['Ohio', 'Colorado'])
print(data.drop(['Ohio', 'Colorado']))

print(data.drop('two', axis=1))
print(data.drop(['two', 'four'], axis='columns'))
obj.drop('c', inplace=True)
print(obj)

###索引的选择与过滤
obj = pd.Series(range(4), index=['a', 'b', 'c', 'd'])
print(obj['b'])
print(obj[1])
print(obj[2:4])
print(obj[['b', 'a', 'd']])
##
obj[['b', 'c']] = 5
print(obj < 2)
###值选择
print(obj[obj < 2])

data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
####根据列选择
print(data['two'])
print(data[['three', 'one']])
###切片选择
print(data[:2])
##值选择
print(data[data['three'] > 5])

#####使用loc轴标签和iloc整数标签选择数据,用loc和iloc运算符分别用于严格处理基于标签和基于整数的索引
print(data.loc['Colorado', ['two', 'three']])
print(data.iloc[2, [3, 0, 1]])
print(data.iloc[2])
print(data.iloc[[1,2],[3,0,1]])
print(data.loc[:'Utah','two'])
print(data.iloc[:,:3][data.three>3])

###整数索引





















