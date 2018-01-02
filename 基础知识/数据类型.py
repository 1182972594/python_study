#!user/bin/python
# python 的数据类型
# 数字 有符号整型（int） 长整型（long）  浮点型（float） 复数（complex）
shuzi = 10
shuzi1 = -10
shuzi_long = 1182972594
shuzi_float = 1234.4546
shuzi_complex = 12 + 10j
print(shuzi, shuzi1, shuzi_long, shuzi_float, shuzi_complex)

# 字符串String
string = 'I Love Yingying'
# python字符串的索引两种方式：1、从左往右索引，默认0开始，最大范围未字符串长度减1；2、从右往左索引，默认从-1开始，最大范围为字符串开头
print(string[2: 6])
print(string*2)             # 字符串输出两次
print(string + '这是真的')
print(string[2:])

# Python 列表（List）
# list 是复合数据类型,可以改变
date_list = ["string", 2, 1.23, 12+10j, 76547283428]
print(date_list)
print(date_list[1:3])
print(date_list*2)
print(date_list+["hahahah", 'end'])
date_list[2] = 1000
print(date_list[2])

# Python 元组(tuple)
tuple_00 = ("nihao", 12, 33.22, 22-4j)
tuple_01 = ('end')
print(tuple_00)
print(tuple_00[2:3])
# tuple_00[0] = 'hahha'  元组数据不可修改
print(tuple_00[0])


# Python 字典（dictionary），可以修改
dictionary = {'key': 'value', 'madan ': 'cao', ' shuzi ': 1}
dic = {}
dic['one'] = 1
dic[2] = 'two'
print(dic['one'])
print(dic[2])
print(dic.keys())
print(dic.values())

# 数据类型的转换
string1 = str(shuzi_long)
print(str(shuzi_long))
print(int(shuzi_long))
print(float(shuzi))
# print(long(shuzi_float))
# 注：type()不会任认为子类是一种父类类型；isinstance()会认为子类是一种父类类型;可用这两个函数判断数据是什么类型

# 小结：python一般6种数据类型number，string，list，dictionary，tuple,file;用的最多的是list,tuple只可读不可写
