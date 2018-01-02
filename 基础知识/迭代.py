# !user/bin/python
# 索引迭代
l =['C', 'java', 'C++', 'python', 'scala']
for index, name in zip(range(1,len(l)+1),l):
    print(index, '-', name)

# 迭代字典中的value
di = {'课程1': 'java', '课程2': 'c++', '课程3': 'c', '课程4': 'python', '课程5': 'c#'}
for m in di.values():
    print(m)

# 计算所有学生的平均分
s_data = {'marry': 68, 'jerry': 75, 'hely': 89, 'kury': 87, 'lpp': 89}
sum = 0;
for d in s_data.values():
    sum += d
print(sum/len(s_data))

# 打印出名称分数和平均数
sum_sum = 0
for  name, score in s_data.items():
    sum_sum += score
    print(name, ': ', score)
print('average:', sum/len(s_data))