# -*- coding: UTF-8 -*-
########面向数组编程
import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
print(ys)
z = np.sqrt(xs ** 2 + ys ** 2)
print(z)
plt.imshow(z, cmap=plt.cm.gray);
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2+y^2}$ for a grid of values")
##where 相当于if else
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
result = np.where(cond,xarr,yarr)
print(result)
####将所有的正值替换为2,负值替换为-2
arr = np.random.randn(4,4)
arr_r = np.where(arr>0,2,-2)
print(arr_r)

###仅将正值替换为2
arr_t = np.where(arr>0,2,arr)
print(arr_t)

####聚合函数 sum,mean,std ,var,min,max,argmin,argmax,cumsum,cumprod
arr = np.random.randn(5,4)
##求均值
mean = arr.mean(dtype=np.float)
print(mean)
##求和
sum = arr.sum(dtype=np.float)
print(sum)
##标准差
std = arr.std(dtype=np.float)
print(std)
###方差
var = arr.var(dtype=np.float)
print(var)
##cumsum
cumsum = arr.cumsum(dtype=np.float)
print(cumsum)
##cumprod
cumprod=arr.cumprod(dtype=np.float)
print(cumprod)

####4.3.3布尔值数组方法
arr = np.random.randn(5,4)
print((arr>0).sum())
##any 存在
print((arr>0).any())
##all 全部
print((arr>0).all())

####4.3.4排序
###sort axis : int, optional
##                Axis along which to sort. Default is -1, which means sort along the
##                last axis.
##axis轴,其实就是shape(),默认按照shape元组的-1位排序
arr = np.random.randn(2,3,3)
print(arr)
arr.sort()
print(arr)

###唯一值与其他集合逻辑unique,唯一值排序
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
names_unique = np.unique(names)
print(names_unique)

###  x数组中的值,是否存在于y中 np.inld(x,y)
values_x = np.array([6,0,3,2,5,6])
values_y = np.array([2,3,6])
in_array = np.in1d(values_x,values_y)
print(in_array)

###数组的集合操作
##unique
##intersectld(x,y)           计算x,y的交集,并排序
##unionld(x,y)               计算x,y的并集并排序
##inld(x,y)                  计算x是否包含在y中,并返回一个bool数组
##setdiffld(x,y)             在x中但不在y中的元素
##setxorld(x,y)              异或集,在x或y中,但不属于x,y交集的元素


