# !user/bin/python
import math


def judge_duble(x):
    return x % 2 ==1


lis = filter(judge_duble, [1, 2, 3, 4, 5, 6])
print()
for i in lis:
    print(i)


def sqrt_re(x):
    if (math.sqrt(x)).is_integer():
        return x


lisss = range(1, 101)
lism = filter(sqrt_re, lisss)
for i in lism:
    print(i)