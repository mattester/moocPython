from datetime import datetime,date,time,timedelta
#自定义日期和时间
d = datetime(2020,10,30,14,5)
print(d)
d2 = date(2019,3,23)
t = time(9,0)
#日期和时间与字符串的相互转换
ds = '2018-10-3 13:44:09'
ds_t = datetime.strptime(ds,'%Y-%m-%d %H:%M:%S')
print(ds_t)

#datetime 对象转换成字符串
n = datetime.now()
print(n)
n_str = n.strftime("%M")
print(n_str)

#datetime 之间的加减操作
n = datetime.now()
n_next = n + timedelta(days=5,hours=42)
print(n_next)

#时间的减法
d1 = datetime(2018,10,5)
d2 = datetime(2018,11,12)
rest = d2 -d1
print(rest)
print(rest.days)
