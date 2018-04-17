# !user/bin/python
class Person(object):
    count = 0

    @classmethod     # 类方法的定义需要在方法定义前添加@classmethod,且方法的第一个且必须有的参数：cls
    def how_many(cls):
        return cls.count

    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1


print(Person.how_many())
p1 = Person('Bob')   # 实例化之后相当于初始化了，调用了方法__init__()方法，所以，count的值会+1，或者cls.count = Person.count
print(Person.how_many())   #类方法跟类属性一样，既可以被实例调用，也可以被类直接调用
print(p1.how_many())
