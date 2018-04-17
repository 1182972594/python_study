# !user/bin/name


class Person(object):
    address = 'china'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


print(Person.address)   # 类属性不需要实例就可以被调用，且所有的实例都可以访问类属性

p1 = Person('baba', '12', '男')
print(p1.address)
print(p1.name)

Person.address = 'beijing'     # 动态修改类变量

print(Person.address)

p1.address = '郑州'  # 若修改了实例属性相当于给该实例创建了一个该属性，而类属性并不受影响，所以不能通过修改实例属性来达到修改雷属性的目的

print(p1.address)
print(Person.address)