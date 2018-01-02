#!user/bin/python
# python的条件判断语句
# if·····else·····
false_flag = False
true_flag = True
name = 'maomao'
a = 5
if false_flag == False:
    print(name)
else:
    print(name*2)

if name =='maomao':
    print(true_flag)
else:
    print(false_flag)

if a > 5:
    print(false_flag)
elif a <= 5:
    print(true_flag)
