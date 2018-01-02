#!user/bin/python
list_my = ['java', 'c', 'C#', 'python', 'c++', 'hadoop']
list_your = ['hive', 'pig', 'scala']
print(list_my[1])
print(list_my[:2])
list_my[2] = 'spark'
print(list_my)
del list_my[2]
print(list_my)
print(list_my + list_your)
my_list = [12, 12, 23, 34, 54]
my_list.append(7777)
print('结果', my_list)
print('统计元素在其中出现的次数', my_list.count(12))
my_list.insert(5, 66)
print(my_list)