# !user/bin/python


# 父类Person
class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


# 子类Student
class Student(Person):
    def __init__(self, name, sex, grade, score):   # 继承自父类的属性还是需要在子类中的初始化方法中申明的，如name,sex
        super(Student, self).__init__(name, sex)
        self.grade = grade
        self.score = score


s1 = Student('xiaoming', '男', '三年级', 80)
print(s1.score)