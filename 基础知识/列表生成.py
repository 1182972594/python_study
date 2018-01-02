# !user/bin/python
# 生成数字list ,我们一般用range(x,y)函数
for i in range(1, 10):
    print(i)
# 生成有特定规则的list
l = []
for i in range(1, 10):
    l.append(i**3)
for ll in l:
    print(ll)