# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

####  颜色 c  colour
####  点大小 s  square
####  透明度  alpha
####  点形状 marker
height = [161,170,182,175,173,165]
weight = [50,58,80,70,69,55]
plt.scatter(height,weight,s = 20,c = 'g',alpha=0.8,linewidths=1)
plt.show()