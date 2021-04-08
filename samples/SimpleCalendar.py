import calendar
import time

cal = calendar.month(2021, 2)
print(cal)

localTime = time.asctime(time.localtime(time.time()))
print('current time %s ' % localTime)
print("timezone = %d" % time.altzone)
