# !user/bin/python

list = map(lambda x: x*x, [1, 2, 3, 4])
for i in list:
    print(i)


# 匿名函数可以简化代码，不需要明确定义函数；关键字lambda表示匿名函数，lambda后面的第一个x是匿名函数的参数，‘：’后面的x*x是函数的表达式
# 匿名函数不用return来返回值，匿名函数的返回值就是表达式的结果

list_01 = sorted([3, 2, 5, 1, 4, 33], reverse=False)
for i in list_01:
    print(i)

# python3.x中的sorted()函数，sorted(iterable,key,reverse),iterable是任何可以迭代的数据集，reverse是正序还是倒序，true为倒序

# 练习
'''
用匿名函数简化下列代码
def is_not_empty(s):
    return s and len(s.strip()) > 0
filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
'''
list_02 = filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])
for i in list_02:
    print(i)
