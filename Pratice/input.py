import datetime as dt
# oldtime = input('enter old time')
# oldtime2 = int(oldtime)
# print(type(oldtime2))

# start = dt.datetime(oldtime)

import datetime

date_entry = input()
datetime.datetime.strptime(date_entry, "%Y/%m/%d")

print(datetime.datetime.strptime(date_entry, "%Y/%m/%d"))