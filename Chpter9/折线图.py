# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#x = np.linspace(-10,10,9)
#y = x**2-2*x+5
#plt.plot(x,y)

###用pandas绘图
s = pd.Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
s.plot()

df = pd.DataFrame(np.random.randn(10,4).cumsum(0),columns=['A','B','C','D'],index=np.arange(0,100,10))
df.plot()
plt.show()