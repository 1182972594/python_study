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


# 子类Book
class Book(Person):
    def __init__(self, name, sex, author):
        super(Book, self).__init__(name, sex)
        self.author = author


b = Book('book', '1', 'author')
p = Person('person', '1')
s = Student('student', '1', '3', 80)
t = Teacher('teacher', '2', 5)



print(type(b.name))
print(type(t.project))  # 通过函数type()获取实例对象属性的类型，通过isinstance()函数判定对象实例是不是某一类型

print(dir(b.name))  # 通过dir()函数，获取对象属性的所有信息,问题：这些信息时干嘛的
print(getattr(b, 'name'))   # 获取实例属性的值，getattr()
setattr(b, 'name', 'hahah')  # 设置实例属性的值，用getattr()
print(b.name)


