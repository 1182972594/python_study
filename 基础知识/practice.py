#!user/bin/python
import math
# 求1*1+2*2+3*3·····99*99+100*100的和
index = 0
result = 0
ll = []
for var in range(100):
    index += 1
    res = pow(index, 2)
    result += res
    ll.append(res)
print(result)
print(ll)

l = [x**2 for x in range(101)]
print(l)
print(sum(l))

lll = [x for x in range(100)]
print(lll)


def re(list):
    l = [x**2 for x in list]
    sum(l)
    print(l)
    print(sum(l))

m_l = range(1, 11)
re(m_l)

# 迭代——汉诺塔
def move(n, a, b, c):
    if n == 1:
        print('a----> c')
        return
    move(n-1, a, c, b)
    print('b----> c')
    move(n-1, b, a, c)
move(3, 'A', 'B', 'C')

# 默认参数
def  great(a, b = 'world!'):
    if b == 'world!':
        print('hello ', b)
    else:
        print('hello' + a)
great('xxx', 'canshu')

# 迭代——输出数字
def get(i):
    if(i<=100):
        print(i)
        i+=1
        get(i)
        if(i%7==0):
            print(i)
    else:
        return 'over'
get(1)