# !user/bin/python
import types
# 定义一个函数


def fun(name, score):
    if name == 'xiaoming':
        print('xiaoming')
    if score < 80:
        print('你是个菜鸡！！')


class Student(object):
    def __init__(self, name, score):   # 相当于Java中的构造方法
        self.name = name
        self.score = score
        self.getMyGrade = lambda: 'A'


s1 = Student('helle', 78)   # 实例化时必须初始化参数
s1.getGrade = types.MethodType(fun, s1)   # 这种转化基本不用

print(s1.getGrade)
print(s1.getMyGrade())


