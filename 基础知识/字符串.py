#!user/bin/python
string = 'Ilovepython'
print(string[:3])
print(string[2:])
print(string[2:5])


l = 0
for letter in string:
    if letter == 'p':
        index = string.index('p')
        print(index)
        print(string[:index])
        print(string[:index] + "runnoob")
        print(l)
    l += 1
print('这是转义符\r')
print('这是一个传参的的字符串第%d行，字符串是%s' % (5, '刘莹莹'))
print(string.center(100))
print(string.capitalize())
print(len(string))