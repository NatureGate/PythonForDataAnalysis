# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np


def createDataFrame():
    frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), index=['Utah', 'Ohio', 'Texas', 'Colorado'],
                         columns=list('bde'))
    return frame


##创建正态
def createNomalDataFrame():
    frame = pd.DataFrame(np.random.randn(4, 3), index=['Utah', 'Ohio', 'Texas', 'Colorado'],
                         columns=list('bed'))
    return frame


def printDataFrame(df):
    print(df)


def printSeries(s):
    print(s)


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
print(data.iloc[[1, 2], [3, 0, 1]])
print(data.loc[:'Utah', 'two'])
print(data.iloc[:, :3][data.three > 3])

###整数索引

###算数和数据对齐 ,类似于外连接
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.3, 3.6, -1.4, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1 + s2)

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), index=['Ohio', 'Texas', 'Colorado'], columns=list('bcd'))
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), index=['Utah', 'Ohio', 'Texas', 'Colorado'], columns=list('bde'))
print(df1 + df2)

print(df1 * df2)
########使用填充值的算数方法,就是将算得的NAN替换为一个特定的值
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df1.loc[1, 'b'] = np.nan
print(df1)
print(df2)
print(df1 + df2)
print(df1.add(df2, fill_value=0))

df1.reindex(columns=df2.columns, fill_value=0)

############################算数方法################$$$$$$$$$$$$$
## add radd 加法
## sub rsub 减法
## div rdiv   除
## floordiv rfloordiv 整除
## mul ,rmul  乘法
## pow , rpow 幂次方
########################################################################
####### DataFrame 与Series 间的操作
arr = np.arange(12.).reshape((3, 4))
###当我们减去arr[0]时,减法在每一行都进行了操作.这就是所谓的广播机制.DataFrame 和Series间的操作是类似的

arr2 = arr - arr[0]
print(arr2)

frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), index=['Utah', 'Ohio', 'Texas', 'Colorado'], columns=list('bde'))
print(frame)
series = frame.iloc[0]
print(series)
##默认情况下,DataFrame 和Series的数学操作中会将Series的索引和DataFrame的列进行匹配,并广播到各行
new_Frame = frame - series
print(new_Frame)

##如果一个索引值不在DataFrame 的列中,也不在Series 的索引中,则对象会重建索引并形成联合
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
print(frame - series2)
##
series3 = frame['d']
##frame.sub(series3,axis = 'index')

############函数的应用和映射
########     Numpy的通用函数(逐元素数组法)对pandas对象也有效
frame = createNomalDataFrame()
printDataFrame(frame)
np.abs(frame)
#####将函数应用到一行或一列的一维数组上.DataFrame的apply方法可以实现这个功能
f1 = lambda x: x.max() - x.min()
print(frame.apply(f1))


###传递给apply的函数并不一定要返回一个标量值,也可以返回带多个值的Series
def f2(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])


print(frame.apply(f2))

format = lambda x: '%.2f' % x
print(frame.applymap(format))

### 排序和排名
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
printSeries(obj)
obj.sort_index()

frame = createNomalDataFrame()
print(frame.sort_index())
printDataFrame(frame.sort_index(axis=1))