# !user/bin/python

class Person(object):
    pass
xiongming = Person()
xionghong = Person()

print(xiongming == xionghong)

'''
定义一个类，创建两个实例，并判断两个实例是否相等
'''

class People:
    pass
xiaoming = People()
xiaoming.name = 'xiaoming'
xiaoming.age = 10
xiaoming.sex = '男'

xiaohong = People()
xiaohong.name = 'xiaohong'
xiaohong.age = 11
xiaohong.sex = '女'

xiaohua = People()
xiaohua.name = 'xiaohua'
xiaohua.age = 12
xiaohua.sex = '男'

r1 = [xiaoming, xiaohong, xiaohua]
r3 = [xiaoming.age, xiaohong.age, xiaohua.age]
r2 = sorted(r3, reverse=True)  #sorted()函数中第一个可迭代的参数类型不能是不能比较大小的
for i in r2:
    print(i)

