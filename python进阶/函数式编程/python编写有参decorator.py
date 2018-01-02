# !user/bin/python
def log(f):
    def my_log(s):
        print('call')
        return print(1)
    return my_log

@log(" ")
def my_fun():
    print('my_fun')