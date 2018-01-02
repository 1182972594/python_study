#!user/bin/python

import random
'''
num = int(random.uniform(1, 100))
print(num)
input_num = int(input("输入数据："))
'''
a = 0
b = 5
c = 11
sum_00 = 0
# while 循环
'''
while b < 10:
    print('输出打印的值为：', b)
    b = b + 1
    print(b)
else:
    print(a)

while num < input_num:
    num += 1
    print(num)
    if num < input_num:
        print('随机小于输入')
    if num > input_num:
        print("随机大于输入")
    if num == input_num:
        print('随机等于输入')
'''
# for 循环
for letter in 'python':
    print('当前字母为：', letter)
fruits = ['香蕉', '苹果', '水蜜桃', '葡萄', '橘子', '火龙果']
leng = len(fruits)
for index in range(leng):
    print("当前水果：", fruits[index])

# 嵌套循环
for num in range(10, 20):   # range()函数是取范围内的开始到结束的所有整数
    for i in range(2, 10):
        if num % i == 0:
            j = num/i
            print('%d 等于 %d * %d' % (num, j, i))
            break
    else:
        print(num, '是质数')

for x in range(1, 3):
    for y in range(1, 3):
        print("这是什么鬼？")
x = 2
i = 1
while x < 4:
    x += 1
    print("这是第", i, "个x")
    i += 1
# 控制语句：break,continue,pass  :
for x in range(1, 8):
    x += 1
    if x == 5:
        print('结束')
        break
        print('$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('############')

# continue语句跳出本次循环，而break跳出整个循环
name = 'python'
for letter in 'python':
    if letter == 't':
        print('before')
        continue
        print('after')
    print(letter)
print('break语句块')
for letter in 'python':
    if letter == 't':
        print('before')
        break
        print('after')
    print(letter)
print('pass语句块')
for letter in 'python':
    if letter == 't':
        print('before')
        pass
        print('after')
    print(letter)