# -*- coding: UTF-8 -*-
import  numpy as np
import  matplotlib.pyplot as plt

###设置刻度标签图例
####对于大多数图表的修饰工作,有两种主要的方式:使用程序性的pyplot接口和更多面向对象的原生matplotlib API
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(np.random.randn(1000).cumsum())
##plt.show()
## 改变x轴的刻度,最简单的方法是使用set_xticks 和set_xticklabels ,set_xticks 表示在数据范围内设定刻度的位置,默认
## 情况下,这些刻度也有标签.但是我们可以使用set_xticklabels 为标签赋值
tick_arr = range(0,1250,250)
ticks = ax.set_xticks(tick_arr)
labels = ax.set_xticklabels(['one','two','three','four','five'],rotation = 30,fontsize = 'small')

ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')
plt.show()

###轴类型有个set方法,允许批量设置绘图属性.根据之前的示例,我们可以写如下代码
props = \
    {
        'title':'My first matplotlib plot',
        'xlabel':'Stages'
    }

ax.set(**props)

