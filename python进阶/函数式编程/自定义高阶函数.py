# ！user/bin/python
# 高阶函数就是能以函数作为参数的函数，即所传的参数可以是函数
import  math
def add(x, y, f):
     return print(f(x) + f(y))
add(-2,5,abs)

def my_sqrt(x, y, f):
     print(f(x)+f(y))
     print(f(x))
     print(f(y))
my_sqrt(4, 9, math.sqrt)

def fx(x) :
     return x*x
li = map(fx,[1,2,3])
for i in li:
     print(i)
def format_name(s):
     return s[0].upper() + s[1:].lower()
ss = map(format_name,['boy','huEEy'])
for i in ss:
     print(i)

def name_format(s):
     return s.capitalize()    # 首字母大写，剩下的全部小写
lis = map(name_format,['GIRL', 'YingYing'])
for i in lis:
     print(i)