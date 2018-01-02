#!user/bin/python
my_tuple = (12, 23, 343, 54, 65, 76, 7)
your_tuple = ('a', 'b', 'c', 'd')
print(my_tuple[:2])
print(my_tuple[2:4])
print(my_tuple + your_tuple)
# tuple 不支持删除操作

# 对元组进行遍历
l = 0
tw = 12
for tw in my_tuple:
    print(my_tuple[l])
    l += 1