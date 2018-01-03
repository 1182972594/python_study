# !user/bin/python
# 利用异常错误，将导入得不正确得得以重新导入
try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO   # 3.x版本中得StringIO 模块已经整合到io中了


'''
所谓得动态导入，就是利用各种异常错误，执行异常情况之外的导入模块代码
'''