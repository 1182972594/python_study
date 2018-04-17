# !user/bin/pyhton
class A(object):
    def __init__(self, one):
        self.one = one


class B(A):
    def __init__(self, one, two):
        A.one = one
        self.two = two


class C(A):
    def __init__(self, one, three):
        A.one = one
        self.three = three


# D类同时继承C类和B类，但是，由于B、C类继承自A类，所以D类也具有A类的属性
class D(B, C):
    def __init__(self, one, two, three, four):
        B.one= one
        B.two = two
        C.three = three
        D.four = four


d = D(1, 2, 3, 4)
print(d.one)
print(d.two)
print(d.three)
print(d.four)

# 类的多继承可以进行功能组合，避免繁琐的代码

