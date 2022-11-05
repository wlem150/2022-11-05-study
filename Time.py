import datetime
import time
from datetime import timedelta
def get_tommrow():
    a =time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(a)

# a = time.localtime(time.time())
# print(a)

b = time.strftime("%c".format(time.localtime(time.time())))
print(b)
# Sat Nov  5 22:55:23 2022
c = datetime.datetime.today()
print(c)
d = datetime.datetime.now()
print(d)
# 2022-11-05 22:55:23.859389

f = datetime.datetime(2018,5,19) # 특정시간을 만들 수 있음
print(f)
g = datetime.datetime.strptime('2018-05-19', '%Y-%m-%d')
print(g)
#2018-05-19 00:00:00

h = g.strftime('%Y-%m-%d')
print(h)

today = datetime.date.today()
get_tommorow = today + timedelta(days=1)
# 오늘과 정한 일수와의 격차를 나타냄
# days=1 하루뒤의 날짜를 출력함

today = datetime.date.today()
get_yesterday = today - timedelta(days=1)
# 어제의 날짜를 출력함