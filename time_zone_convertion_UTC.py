import pytz, datetime
local = pytz.timezone ("Asia/Singapore")
naive = datetime.datetime.strptime ("2019-02-03 10:11:12", "%Y-%m-%d %H:%M:%S")
local_dt = local.localize(naive, is_dst=None)
utc_dt = local_dt.astimezone(pytz.utc)
str_utc = utc_dt.strftime ("%Y-%m-%d %H:%M:%S")
print (str_utc)
