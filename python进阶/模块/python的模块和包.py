# !user.bin/python
import math
import time
# 一个.py文件就是一个模块；引用其他模块用import 关键字
def my_pow(x):
    return math.sqrt(x)

s = my_pow(9)
print(s)

time_01 = time.localtime()
print(time.strftime('%Y-%m-%d %H:%M:%S', time_01))


'''
import math
math.pow()
'''