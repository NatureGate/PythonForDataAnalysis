# -*- coding: UTF-8 -*-
import  pandas as pd
import  numpy as np
from pandas import  Series,DataFrame
###  Series是一个既包含数组,也包含dict的结构
##   既可以随机访问,也可以通过hash访问 ..
obj = pd.Series([2,4,6,1,-3])
print(obj)
print(obj.values)
print(obj.index)
obj2 = Series([1,2,3,4,],index=['a','b','c','d'] )
print('get a = '+str(obj2['a']))
print(obj2[['a','b','c']])
###数学函数
print(obj2>3)
print(obj2*3)
print(np.exp(obj2))
print(np.sin(obj2))
###使用dic创建Series
sdata = {'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
obj3 = Series(data=sdata)
print(obj3)
###将指定的顺序传递给构造函数,通过字典和特定索引创建
states = ['California','Texas','Utah','Oregon']
obj4 = Series(data=sdata,index=states)
print(obj4)
##检查缺失数据
print(pd.isnull(obj4))
print(obj4.isnull())

##索引对齐,当两个索引相同,但是其中一个为NAN时,计算结果为NAN
print(obj4+obj3)

###Both Series and it's index have name

obj4.name = 'population'
obj4.index.name = 'state'
print(obj4.name)
print(obj4.index.name)

##索引可以按照位置复制改变
obj.index = ['Bob','Steve','Jeff','Ryan','Joy']

##########  DataFrame ,有点像带索引的数据库表
##########
##########
data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],'year':[2000,2001,2032,2001,2002,2003],'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
frame = pd.DataFrame(data)
print(frame)
print(frame.head(3))
##指定DataFrame的列将会按照指定顺序排列
frame2 = pd.DataFrame(data,columns=['year','state','pop'])
print(frame2)

###你传的列不包含在字典中,将会在结果中出现缺失值
frame3 = pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five','six'])
print('frame3++++++++++++++++++++++++++++++++'+str(frame3))
##DataFrame 中的一列,可以按照字典型标记或属性那样检索为Series
print(frame2['state'])
print(frame2.pop)
###注意frame.column只有在列是有效的Python变量名时可用,否则会抛出属性错误
#print(frame2.debt)

###也可以通过索引进行选取 loc
print(frame3.loc['three'])

##列的值是可以修改的
frame3.debt = '16.5'
print(frame3)
val = pd.Series([2.2,3.3,4.4],index=['two','three','four'])
frame3.debt = val
print(frame3)
del frame3['debt']
print(frame3)

###包含字典的嵌套字典
pop = {'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame4 = pd.DataFrame(pop)
print(frame4)

###转置
print(frame4.T)

frame5 = pd.DataFrame(pop,index=[2001,2002,2003])
print(frame5)

pdata = {'Ohio':frame4['Ohio'][:-1],'Nevada':frame4['Nevada'][:2]}
frame6 = pd.DataFrame(pdata)
print(frame6)

####索引对象
obj = pd.Series(range(3),index=['a','b','c'])
index = obj.index
print(index)
#### index数组不可变 Index does not support mutable operations
#### index[0] = 'd'

###index对象除了可以看成数组,也可以看成集合
inda = pd.Index([2,3,4,5])
indb = pd.Index([7,3,9,4])

print(inda.append(indb))
print(inda.difference(indb))##差集
print(inda.intersection(indb))##交集
print(inda.union(indb))##并集
print(inda.delete(0))
print(inda.is_monotonic)



