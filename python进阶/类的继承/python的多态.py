# !user/bin/python


# 父类Person
class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def whoAmi(self):
        return 'i am %s ' % self.name


# 子类Student
class Student(Person):
    def __init__(self, name, sex, grade, score):   # 继承自父类的属性还是需要在子类中的初始化方法中申明的，如name,sex
        super(Student, self).__init__(name, sex)
        self.grade = grade
        self.score = score

    def whoAmi(self):
        return 'i am %s ' % self.name


# 子类Teacher
class Teacher(Person):
    def __init__(self, name, sex, project):
        super(Teacher, self).__init__(name, sex)
        self.project = project

    def whoAmi(self):
        return 'i am %s ' % self.name


class Book(Person):
    def __init__(self, name, sex, author):
        super(Book, self).__init__(name, sex)
        self.author = author


b = Book('book', '1', 'author')
p = Person('person', '1')
s = Student('student', '1', '3', 80)
t = Teacher('teacher', '2', 5)

def who_am_i(x):
    print(x.whoAmi())


who_am_i(p)
who_am_i(s)
who_am_i(t)
who_am_i(b)   # 子类调用多态的方法时，首先在自己类中寻找，自身没有定义实现时就调用父类的



'''
print(p.whoAmi())
print(s.whoAmi())
print(t.whoAmi())
'''


'''
像下面一样，通过传入一个参数，能够对对应的实例的方法进行调用就叫python的多态， 感觉比较傻
def who_am_i(x):
    print(x.whoAmi())


who_am_i(p)
who_am_i(s)
who_am_i(t)
'''


import json

class Students(object):
    def read(self):
        return r'["Tim", "Bob", "Alice"]'

s = Students()    # 由于Python的动态特性，json.load()并不一定要从一个File对象读取内容。任何对象，只要有read()方法，就称为File-like Object，都可以传给json.load()。

print(json.load(s))
