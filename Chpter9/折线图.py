# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,9)
y = x**2-2*x+5
plt.plot(x,y)
plt.show()