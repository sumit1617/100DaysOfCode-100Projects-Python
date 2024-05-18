import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
sec = now.second
min = now.minute


data_of_birth = dt.datetime(year=2002, month=7, day=6, hour=20, second=45, minute=31)
print(data_of_birth)