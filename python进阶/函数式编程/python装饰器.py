# !user/bin/python

# 装饰器就是利用高阶函数来实现对已经定义的函数进行功能扩展

def f2(f):
    def my_log(x):
        print('log')
        return f(x)
    return my_log

@f2
def f1(x):
    return print(x*x)


f1(2)



