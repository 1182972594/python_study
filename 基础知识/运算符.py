#!user/bin/python
# python 运算符

# 算术运算符：+（加），-（减），*（乘），/（除），%（求余），**（次方），//（取商，商的整数部分）
five = 19
four = 4
print("求和的结果是：", five+four)
print("求差的结果是：", five-four)
print("求积的结果是：", five*four)
print("相除的结果是：", five/four)
print("求余的结果是：", five%four)
print("次方的结果是：", 2**10)
print("求商的结果是：", five//four)
# 比较运算符：==，！=，<>，<,>,>=,<=
print("19等于4吗？", five == four)
print("19不等于4吗？", five != four)
print("19大于4吗？", five > four)
print("19小于4吗？", five < four)
print("19小于等于4吗？", five <= four)
print("19大于等于4吗？", five >= four)
# 赋值运算符:=(简单的赋值运算符),+=（加法赋值运算符）,-=,*=,/=,**=,//=
# 位运算符：&(与),|(或),^(异或运算),~(按位取反),<<(左移运算),>>(右移运算),重要针对二进制的数据进行运算
# 逻辑运算符：and , or ,not
a = 19
b = 4
c = 4
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
if a and b:
    print(a and b)
if a or b:
    print(a or b)
# 身份运算符 ： is ,is not

# 成员运算符：in ，not in
if b in l:
    print('b存在于列表l中')
else:
    print('b不存在于列表l中')

if b not in l:
    print('b不存在于l中')
else:
    print('b存在于l中')

if b is c:
    print('b和c拥有相同的标识符')
else:
    print('b和c没有相同的标识符')

if b is not c:
    print('b和c没有相同的标识符')
else:
    print('b和c拥有相同的标识符')