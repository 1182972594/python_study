# !user/bin/python
# reduce高阶函数传入的参数函数必须有两个参数
from functools import reduce  # reduce()高阶函数再python3.x之后已经不在built_infunction中了，需要导入


def add_sum(x, y):
    return x + y


liss = reduce(add_sum, [1, 2, 3, 4, 5])
print(liss)


def getChengji(x, y):   # 函数定义的前后一定要留两空行
    return x * y


def getXY():
    result = reduce(getChengji, [1, 2, 3, 4], 2)  # reduce()的第三个参数是初始值，可以有也可以没有
    print(result)
getXY()
