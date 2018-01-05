# !user/bin/python
class Person(object):
    def __init__(self, year, height, weight):
        self.year = year
        self.height = height
        self.__weight = weight    # 私有属性

    def group(self, year, height, weight):   # 定义实例方法，实例方法只能通过实例来调用
        self.yead = year
        self.__weight = weight + height
        return  self.__weight   # 通过实例方法可以调用私有属性（有访问限制的属性）

p1 = Person(15, 175, 55)

print(p1.group(15, 175, 55))


# ***************************************************************

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score =score

    def getGrade(self):
        if self.__score > 80:
            return 'A'
        if self.__score <= 80:
            return 'B'


p2 = Student('bobo', 80)

print(p2.getGrade())