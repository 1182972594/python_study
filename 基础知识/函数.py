#!user/bin/python
import math
import operator
import random

def add(var1, var2):
    sum_1_2 = var1 + var2
    cha = var2-var1
    cheng = var1 * var2
    chu = var2/var1
    print(sum_1_2, cha, cheng, chu)
# 调用函数前面需要有两个空行


add(2, 4)
la = [1, 2, 3, 4, 5, 6]  # list
print(la)
la[2] = 88
print(la)

num = 12
print('类型转换为整型', int(12))
print('类型转换为字符串', str(12))
print('类型转换为浮点型', float(12))
print('类型转换为复数', complex(12))
print('类型转换为表达式字符串', repr(12))
print('序列转换为列表', list([1, 2, 3]))
print('列表转换为元组', tuple(['a', 'b', 'c']))
print('字符转换为数字', ord('9'))
print('字符转换为数字', ord('a'))    # 转换的是代表的asc表对应的字符和数值
print('数字转换为字符', chr(97))

# 常用的内置函数
print('求绝对值：', abs(-10))
print('进一取整', math.ceil(4.1))
print('比较大小', operator.eq(4, 5))   # 如果x<y,返回-1；如果x>y，返回1；如果x==y,返回0
print('x<y', operator.lt(4, 5))
print('x>y', operator.le(4, 5))
print('返回e的x次幂的结果', math.exp(1))
print('平方', pow(2.718281828459045, 2))
print('返回绝对值的结果为浮点型', math.fabs(-10))
print('退一取整', math.floor(4.9))
print('返回次方值', math.log(1024, 2))
print('多次方值', pow(2, 100))
print('四舍五入', round(3.2))
print('开方', math.sqrt(144))

print('随机数', random.random()*100)   # random（）生成的是0~1之间的数
print('随机数11', random.uniform(1, 5))
print('随机整数', random.choice(range(100000)))

print('常量pi', math.pi)
print('常量e', math.e)