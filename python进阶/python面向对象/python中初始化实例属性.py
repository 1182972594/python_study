# !user/bin/python
class Person:
    def __init__(self, name, age, sex, address):  # 用__init__(self)方法定义属性
        self.name = name
        self.age = age
        self.sex = sex
        self.address = address

p1 = Person('xiaoming', 10, '男', '中国')   # 在实例化中初始化属性

p2 = Person('xiaohua', 11, '女', '中国台湾')

print(p1.age)
print(p1.name)
