from datetime import datetime,time
x=datetime.now()
y=datetime.strptime('2023-03-08 02:02:02','%Y-%m-%d %H:%M:%S')
z=(x-y).seconds+(x-y).days*86400
print(z)