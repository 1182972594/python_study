# !user/bin/python
def my_out():
    print('外函数')
    def my_in():
        print('内函数')
        def my_in_in():
            print('my_in_in')
        my_in_in()
    my_in()
    return my_in()
my_out()


print('***********************************************')
# 返回函数可以延迟计算
def my_hanshu():
    def my_my():
        print('内函数')
    return my_my
my_hanshu()