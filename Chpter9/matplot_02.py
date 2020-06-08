# -*- coding: UTF-8 -*-
import  numpy as np
import  matplotlib.pyplot as plt

#    创建子图 nrows=1, ncols=1, sharex=False, sharey=False, squeeze=True,
#             subplot_kw=None, gridspec_kw=None, **fig_kw
fig ,axes = plt.subplots(nrows=2, ncols=2)
##调整子图周围的间距
##axes.subplots_adjust()
##
fig,axes = plt.subplots(2,2,sharex=True,sharey=True)
for i in range(2):
    for j in range(2):
        axes[i,j].hist(np.random.randn(500),bins=50,color = 'k',alpha = 0.5)
plt.subplots_adjust(wspace=0,hspace=0)


