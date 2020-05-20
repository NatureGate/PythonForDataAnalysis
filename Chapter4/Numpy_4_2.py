# -*- coding: UTF-8 -*-
#######通用函数ufunc,逐元素替换函数
#一元函数
##    函数名
##    abs fbs
#    sqrt
#    square
#    exp
##    log/log10/log2/log1p
##    sign
##    ceil
##    floor
##    rint
##    modf
##    isnan
##    isfinite/isinf
##    cos/cosh/sin
##    sinh/tan/tanh
##   arccos/arccosh/arcsin
##    arcsinh/arctan/arctanh
##    logical_not

####################################################################################
##############二元通用函数
##函数名
#add
#subtract                  在第二个数组中,将第一个数组包含的元素去除
#multiply                  将数组的对应元素相乘
#divide,floor_divide       除或整除
#power
#maximun,fmax              逐个求最大值,忽略NAN
#minimum ,fmin             逐个求最小值,忽略NAN
#mod
#copysign                   将第一个数组的符号值,改为第二个数组的符号值
#greater,greater_equal,less 逐个元素比较,返回布尔值
#less-equal,equal,not_equal 操作符 >,>=,<,<=,==,!=
#logical_and ,logical_or,logical_xor    将逐个元素逻辑操作