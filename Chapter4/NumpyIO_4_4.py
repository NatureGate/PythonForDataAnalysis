# -*- coding: UTF-8 -*-
import numpy as np
##########使用数组进行文件输入和输出
###np.save和np.load是读写磁盘数组数据的两个主要函数。默认情况下，
# 数组是以未压缩的原始二进制格式保存在扩展名为.npy的文件中的

arr = np.arange(10)
arr2 = np.arange(20)
##创建文件写入数据
np.save('some_arry',arr)
##读取文件
array = np.load('some_arry.npy')
print(array)
##使用savez并将数组作为参数传递给该函数,用于在未压缩文件中保存多个数组
##有点像properties文件,map
np.savez('array_txt',a = arr,b =arr2)
arch = np.load('array_txt.npz')
print(arch['b'])