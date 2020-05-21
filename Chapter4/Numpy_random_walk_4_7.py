# -*- coding: UTF-8 -*-
import  random
position = 0
steps = 1000
walk = [position]
for i in range(steps):
     step = 1 if random.randint(0,1) else -1
     position += step
     walk.append(position)

###简单随机漫步
