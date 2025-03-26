import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()
time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S:%p %m-%d-%Y")
target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 0)
current_datetime = datetime.datetime.now()
if target_datetime < current_datetime:
    print("Target datetime has passed.")
else:
    print("Target datetime is in the future.")
print(date)
print(now)