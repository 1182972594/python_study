#!user/bin/python
dic = {'key1': '妖精的尾巴', 'key2': '海贼王', 'key3': '火影忍者'}
info_dic = {'name': '木刻川川', 'age': '24', 'sex': '男', 'isGF': '是'}
# 修改字典中的元素
dic['key1'] = '变形金刚'
print(dic['key1'])
# 添加字典中新元素
dic['key4'] = '赤红之瞳'
print(dic)
#删除字典中的元素
del dic['key2']
print(dic)
# 获取字典的长度
print(len(dic))