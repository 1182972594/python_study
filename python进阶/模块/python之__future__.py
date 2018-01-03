# !user/bin/python
from __future__ import unicode_literals
# 将代码中的字符串转化为unicode
s = 'i am a good man'
print(isinstance(s, str))  # 已经转化为unicode了，为啥，判断是否为字符串，返回值仍为True?


'''
__future__的导入就是能够使用高版本的新功能；
unicode是一种编码方式，如utf-8,gbk,utf-16等；
python中使用unicode编码的好处时便于跨平台，python用两个字节去存储Unicode
decode,encode

'''