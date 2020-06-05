# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
from numpy import nan as NA

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
data = pd.Series([1, NA, 3.5, NA, 7])
print(data.dropna())

###删除包含缺失值的行
data = pd.DataFrame([[1,6.5,3.],[1.,NA,NA],[NA,NA,NA],[NA,6.5,3]])
cleaned = data.dropna()
print(cleaned)
###传入how='all'是,将删除所有值为NA的行, axis=0, how="any", thresh=None, subset=None, inplace=False
print(data.dropna(how='all'))
df = pd.DataFrame(np.random.randn(7,3))
df.iloc[:4,1] = NA
df.iloc[:2,2] = NA
print(df)
print(df.dropna())
print(df.dropna(thresh=2))


####补全缺失值 fillna
print(df.fillna(0))

###为不同的列设置不同的填充值
print(df.fillna({1:0.5,2:0}))

###修改一个已经存在的对象 inplace = true
_ = df.fillna(0,inplace=True)
print(df)

df = pd.DataFrame(np.random.randn(6,3))
df.iloc[2:1] = NA
df.iloc[4:2] = NA
print(df)
print(df.fillna(method='ffill'))
print(df.fillna(method='ffill',limit=2))

###########
#####   value 标量值或字典型对象用于填充缺失值
######  method 插值方法,如果没有其他参数,默认是ffill
###     axis  需要填充的轴,默认axis=0
####
##################数据转换##########################
##################数据转换##########################
####删除重复值
data = pd.DataFrame({'k1':['one','two']*3+['two'],'k2':[1,1,2,3,3,4,4]})
print(data)
print(data.duplicated())
print(data.drop_duplicates())

data = pd.DataFrame({'food':['bacon','pulled pork','bacon','Pastrami','corned beef','Bacon','pastrami','honey ham','nova lox'],
              'ounces':[4,3,12,6,7.5,8,3,5,6]})
print(data)
meat_to_animal = \
    {
        'bacon':'pig',
        'pulled pork':'pig',
        'corned beef':'cow',
        'honey ham':'pig',
        'nova lox':'salmon'
    }

lowercased = data['food'].str.lower()
print(lowercased)
data['animal'] = lowercased.map(meat_to_animal)
print(data)

############替代值
data = pd.Series([1.,-999,2.,-999,-1000,3.])
data.replace([-999,-1000],[np.nan,0])
############重命名轴索引

















