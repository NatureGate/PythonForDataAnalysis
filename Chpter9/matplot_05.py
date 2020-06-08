# -*- coding: UTF-8 -*-
import  numpy as np
import  matplotlib.pyplot as plt

###添加图例
from numpy.random import randn

###添加图例
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(randn(1000).cumsum(),'k',label = 'one')
ax.plot(randn(1000).cumsum(),'g--',label = 'two')
ax.plot(randn(1000).cumsum(),'r.',label = 'three',alpha = 1)
ax.legend(loc = 'best')
plt.show()



