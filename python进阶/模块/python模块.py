# !user/bin/python
# 导入一个模块得部分函数
from math import sin, sqrt
import math, logging
print(math.cos(3.1415/3))
print(sqrt(9))
print(sin(3.1415926/3))
# 不同模块得同名函数调用，要加上模块名前缀
print(math.log(2, 3))
logging.log(10, 'message')
'''
# 导入一个模块得具体得某个函数，调用时不需要添加模块名.XXX,直接调用即可。
from math import sin, sqrt
print(sqrt(9))
'''


'''
# 导入一整个模块函数
import math
print(math.sqrt(9))
'''

'''
1导入整个模块
2、导入一个模块中得部分函数
3、不同模块中得同名函数得调用，或者起别名
'''

