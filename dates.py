"""
This example demonstrates how dates and time are used in Python.
"""
import datetime
import pytz

# Simple date object from 'datetime' module
d = datetime.date(2001, 9, 11)
print(f"(2001, 9, 11) date object in 'datetime' Module:\t{d}")
print(f'===>Year(2001, 9, 11):\t{d.year}')
print(f'===>Year(2001, 9, 11):\t{d.month}')
print(f'===>Year(2001, 9, 11):\t{d.day}')
print()

tday = datetime.date.today()
print(f"Today's date in 'datetime' Module: \t{tday}")
print(f'===>Today:\t{tday.day}')

# weekday() - Monday is 0 and Sunday is 6
wday = tday.weekday()
isowday = tday.isoweekday()
print(f'===>Weekday of today:\t{wday}')

# isoweekday() - Monday is 1 and Sunday is 7
print(f'===>ISO weekday of today:\t{isowday}')
print()

# datetime.timedelta(
# days=0, 
# seconds=0, microseconds=0, milliseconds=0, 
# minutes=0, hours=0, weeks=0)

tdelta = datetime.timedelta(days=7, hours=12)

print('7 days and 12 hours from today:\t', tday + tdelta)

bday = datetime.date(tday.year, 12, 20)
till_bday = bday - tday

print("{0} days left till DP's birthday".format(till_bday.days))
print("{0:,.2f} seconds left till DP's birthday".format(till_bday.total_seconds()))
print()

t = datetime.time(9, 30, 45, 100000)
print(f"(9, 30, 45, 100000) time object in 'datetime' Module:\t{t}")

# print( ttime)
# print('Current hour:\t', ttime.hour)

dt = datetime.datetime.today()
dtnow = datetime.datetime.now()
# print(dir(datetime.datetime))
print(f"===>The datetime object of Today in 'datetime' Module:\t{dt}")
print(f"===>The datetime object of Now in 'datetime' Module:\t{dtnow}")
print()

# Timezone-aware format
dt = datetime.datetime(2016, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print('The UTC format of Now with pytz.UTC:\t', dt_utcnow)

dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print('===>utcnow().replace(tzinfo=pytz.UTC):\t', dt_utcnow2)

dt_pac = dt_utcnow.astimezone(pytz.timezone('US/Pacific'))
print("===>astimezone(pytz.timezone('US/Pacific')):\t", dt_pac)
print()

dt_pac = datetime.datetime.now()
pac_tz = pytz.timezone('US/Pacific')
dt = pac_tz.localize(dt_pac)

print('Timezone-aware: Pacific time:\t', dt_pac)
print('==>Local time:\t', dt)

dt_east = dt.astimezone(pytz.timezone('US/Eastern'))
print('Timezone-aware: Eastern time:\t', dt_east)
print()

# strftime - Datetime to String
print('Datetime to String using strftime():\t', dt.strftime('%B %d, %Y'))

# Datetime stamps in readable formats
dt_str = 'July 22, 1983'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print('Datetime ofject in string format using strptime():\t', dt)
