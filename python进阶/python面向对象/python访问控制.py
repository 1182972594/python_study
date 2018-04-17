# !user/bin/python
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score   # 以双下划线（__）为开头命名的属性不能被外部访问


p1 = Person('alice', 89)
print(p1.name)
# print(p1.score)
