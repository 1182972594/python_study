#!user/bin/python
# python 中的数据类型是不允许修改的，如果要修改那就必须要分配新的内存
import time
var1 = 10
var2 = 20
var3 = 30
var4 = 40.123
# 删除单个或者多个对象，删除后的对象将不能再进行引用
del var1, var2
print(var3)
# 小数强转为整数
print(int(var4))
# 强转为字符串
print(str(var4) + '这是字符串')
print("this is a %s world! %d" % ("beautiful", 66))

var = time.time()
print(time.localtime(var))
print('\n')
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))