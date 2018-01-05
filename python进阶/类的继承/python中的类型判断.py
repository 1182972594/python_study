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


p = Person('person', '1')
s = Student('xiaoming', '1', '三年级', 89)

print(isinstance(p, Student))   # 子类的实例同时也是父类的实例，但是父类的实例不是子类的实例
print(isinstance(s, Person))

# python 中通过isinstance()方法来判断一个实例对象的类型
print(isinstance(1, int))  # 判断是不是整形
print(isinstance(1, str))  # 判断是不是字符串