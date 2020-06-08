reference：https://note.nkmk.me/python-datetime-usage/

import datetime

dt_now = datetime.datetime.now()
print(f'datetime.datetime.now() --> {dt_now}') #2020-06-07 19:05:14.421924
print(f'type(dt_now)---> {type(dt_now)}') #<class 'datetime.datetime'>
print(f'dt_now.year---> {dt_now.year}') #2020
print(f'dt_now.month---> {dt_now.month}')#6
print(f'dt_now.day---> {dt_now.day}')#7
print(f'dt_now.hour---> {dt_now.hour}')#19
print(dt_now.minute)
print(f'dt_now.date() ----> {dt_now.date()}')#2020-06-07
    
dt = datetime.datetime(2020, 6, 1)
print(dt) #2020-06-01 00:00:00
print(dt.minute)

d_today = datetime.date.today()
print(f'datetime.date.today() ---> {d_today}') #2020-06-07
print(type(d_today)) #<class 'datetime.date'>
print(f'd_today.year >>> {d_today.year}') #2020

d = datetime.date(2020, 6, 1)
print(d) #2020-06-01
print(d.month) #6

t = datetime.time(12, 15, 20)
print(t) #12:15:20
print(type(t)) #<class 'datetime.time'>
print(t.hour) #12

t = datetime.time()
print(t) #00:00:00

#timedelta, 
td = dt_now - dt
print(td) #6 days, 21:47:11.207976
print(type(td)) #<class 'datetime.timedelta'>
print(td.days) #6
print(td.seconds) #78552

#timedeltaオブジェクトを使った引き算、足し算
td_1w = datetime.timedelta(weeks=1)
print(td_1w) #7 days, 0:00:00

d_1w = d_today - td_1w
print(d_1w) #7 days, 0:00:00

td_10d = datetime.timedelta(days=10)
print(td_10d) #10 days, 0:00:00

dt_10d = dt_now + td_10d
print(dt_10d) #2020-06-17 21:56:06.493474

td_50m = datetime.timedelta(minutes=50)
print(td_50m) #0:50:00
print(td_50m.seconds) #3000

dt_50m = dt_now + td_50m
print(dt_50m) #2020-06-07 22:49:14.598695

#特定の日付までの日数（東京オリンピック開会式まであと何日）みたいな値を算出するのにも使える。
d_target = datetime.date(2020, 7, 24)
td = d_target - d_today
print(td)  #47 days, 0:00:00

#strftime(): 日付、時間から文字列への変換
print(dt_now.strftime("%Y-%m-%d %H:%M:%S"))  #2020-06-07 22:04:52

print(d_today.strftime("%y%m%d")) #200607
print(d_today.strftime("%Y%m%d")) #20200607

print(f'日番号（1年の何日目か／正月が001）　：{d_today.strftime("%j")}')
#日番号（1年の何日目か／正月が001）　：160
print(f'週番号（週の始まりは月曜日／正月が00) : {d_today.strftime("%W")}')
#週番号（週の始まりは月曜日／正月が00) : 23

#文字列ではなく数値を取得したい場合は、int()で整数に変換すればOK。
week_num_mon = int(d_today.strftime("%W"))
print(week_num_mon)
print(type(week_num_mon)) #d_today.strftime("%W")

#timedeltaオブジェクトと組み合わせて、隔週の日付のリストを作るみたいなことも簡単。
d = datetime.date(2020, 6, 3)
td = datetime.timedelta(weeks=2)
n = 8
f = "%Y-%m-%d"

l = []
for i in range(n):
    l.append((d + i * td).strftime(f))
print(l)
#['2020-06-03', '2020-06-17', '2020-07-01', '2020-07-15', '2020-07-29', '2020-08-12', '2020-08-26', '2020-09-09']
print("\n".join(l))

#リスト内包表記を使うともっとスマート。
S = [(d + i * td).strftime(f) for i in range(n)]
print("\n".join(S))
'''
strptime(): 文字列から日付、時間への変換
datetimeのstrptime()を使うと、日付や時刻を表す文字列からdatetimeオブジェクトを生成できる。
元の文字列に対応する書式化文字列を指定する必要がある。
'''
date_str = "2020/6/8 12:30"
date_dt = datetime.datetime.strptime(date_str, "%Y/%m/%d %H:%M")
print(date_dt) #2020-06-08 12:30:00
