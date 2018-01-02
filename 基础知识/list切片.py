#!user/bin/python
l = [x for x in range(1, 101)]
print(l)
print(l[-10:])
print(l[-46::5])     # 确定要从哪一个开始
print(l[19:50:5])    # 从第20个开始取，每隔4个取一个

lll = range(100)
print(lll[1:10])

wh = 'wh'
index = 0
count = 0
word_l = ['what', 'here', 'when', 'why', 'who']
for x in range(len(word_l)):
    if wh in word_l[index]:
        count += 1
    index += 1
print(count)


