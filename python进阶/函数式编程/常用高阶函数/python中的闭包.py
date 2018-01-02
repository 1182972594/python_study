# !user/bin/python
# 函数内部定义的函数不能被外部函数，只能由外部函数返回，然后调用
def my_function():
    def my_fun():
        print('11111')
