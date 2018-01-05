# !user/bin/python

# 子类和父类的关系：子类继承自父类，拥有父类的属性和方法，但是子类拥有一些新的父类没有的方法，子类的实例也时父类的实例，但是父类的实例不是子类的实例
# 类的继承，如下，父类本省的属性在子类中的实现，通过类名.__init__()方法进行实现
class Anminal(object):
    def __init__(self, eat, run):
        self.eat = eat
        self.run = run


class Dog(Anminal):
    def __init__(self, eat, run, sleep, jump):
        super(Dog, self).__init__(eat, run)   # 子类中的super()方法，两个参数，一个时子类本身，一个时self
        self.sleep = sleep
        self.jump = jump


class Cat(Anminal):
    def __init__(self, eat, run, miaomiao):
        super(Cat, self).__init__(eat, run)
        self.miaomiao = miaomiao


c1 = Cat('fish', 'run', 'miaomiao')

d1 = Dog('eat bones', 'run away', 'sleep night', 'jump away')

print(d1.eat)
print(c1.eat)
print(d1.jump)