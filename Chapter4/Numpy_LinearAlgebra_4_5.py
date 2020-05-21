# -*- coding: UTF-8 -*-
import numpy as np

## 4.5 线性代数
###矩阵的乘法
## 0    1   2       0   1
## 3    4   5       2   3
##                  4   5
##
##
##
x = np.arange(6).reshape(2, 3)
y = np.arange(6).reshape(3, 2)
arrd = x.dot(y)
arrc = np.dot(x, y)
print(arrd)
print(arrc)

####numpy.vdot() 函数是两个向量的点积。 如果第一个参数是复数，
# 那么它的共轭复数会用于计算。 如果参数是多维数组，它会被展开。
#  1*11+2*12+3*13+4*14
a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
print(np.vdot(a, b))

##numpy.inner() 函数返回一维数组的向量内积。对于更高的维度，它返回最后一个轴上的和的乘积。
### 等价于 1*0+2*1+3*2
print(np.inner(np.array([1,2,3]),np.arange(3)))
import numpy.linalg as ll
arr = np.array([[1,0,1],[1,1,0],[0,0,1]])
## det 计算行列式
print(ll.det(arr))
## inv 计算逆矩阵
print(ll.inv(arr))
### eig计算特征值和特征向量
print(ll.eig(arr))
### solve 求解 Ax = b,其中A是方阵
A = np.array([[1,2],[3,0]])
b = np.array([1,1])
print(ll.solve(A,b))