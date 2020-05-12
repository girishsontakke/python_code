import datetime
import pytz 

d = datetime.date(2000, 7, 24)
print("d = ", d)

tday = datetime.date.today()
print('today = ',tday)
print('today year = ',tday.year)
print('today weekday =' , tday.weekday())
print('today isoweekday =',tday.isoweekday())

tdelta = datetime.timedelta(days=7)
print('+ timedelta = ',tday + tdelta)
print('- timedelta = ', tday - tdelta) 

bday = datetime.date(2020, 6, 21)
till_bday = bday - tday
print('Days to bday =', till_bday)
print('Days to bday =',till_bday.days)
print('Seconds to bday =', till_bday.total_seconds())

t = datetime.time(9, 30, 10, 100000)
print('t = ', t)
print('hour in t = ', t.hour)
dt = datetime.datetime(2020, 7, 26, 12, 30, 45, 100000)
print('given date = ', dt)
print(dt.second)
print(dt.date())
print(dt.time())
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print('dt_today =',dt_today)
print('dt_now =',dt_now)
print('dt_utcnow =',dt_utcnow)

dt1 = datetime.datetime(2020, 7, 26, 12, 30, 45, tzinfo=pytz.UTC) 
print('dt1 =',dt1)

dt_now1 = datetime.datetime.now(tz = pytz.UTC)
print('dt_now1 = ', dt_now1)
dt_utcnow1 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print('dt_utcnow1 =',dt_utcnow1)

dt_mtn = dt_now1.astimezone(pytz.timezone('US/Mountain'))
print('dt_mtn =',dt_mtn)

# for tz in pytz.all_timezones:
#    print(tz) 

#converting neive time(neive time is time which is not time-zone aware)

dt_mtn1 = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn1  = mtn_tz.localize(dt_mtn1)
# still working without above two operations
dt_east = dt_mtn1.astimezone(pytz.timezone('US/Eastern'))
print('dt_mtn1 =',dt_mtn1)

#isoformat
print(dt_now)
print('dt_now in mentioned formate: ', dt_now.strftime('%B %d %Y'))

date_str = 'July 26 2016'
date2 = datetime.datetime.strptime(date_str, '%B %d %Y')
print('date2 = ', date2)