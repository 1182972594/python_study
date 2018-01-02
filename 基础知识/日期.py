#!user/bin/python
import time
import calendar
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print('Y%-M%-D% %HH:%MM:%SS', time.asctime(time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# 日历
a = calendar.month(2017, 3)
print(a)
print(time.clock())