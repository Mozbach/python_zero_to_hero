# The Python Datetime module... Hopefully it is simpler that Javascript's
import datetime
# In the arguments for datetime, we can pass: [hour[, minute[, second[, microsecond],[tzinfo]]]] -> If we fail to provide one or any of these arguments, they will be filled out automatically
mytime = datetime.time(2, 20) # Here we say it is 2:20am
print(f"My Time: {mytime}")
# This outputs: My Time: 02:20:00

# You can also access various values within your time object, like minutes - for example
print(f"Minutes in mytime: {mytime.minute}")
# This outputs: Minutes in mytime: 20

mytime2 = datetime.time(13, 40, 1, 44)
print(f"My Time 2: {mytime2}")
# Above outputs: My Time 2: 13:40:01.000044


# Working with some date object:
today = datetime.date.today() #within arguments, define year, month and day 
print(f"Today is : {today}")

# Within the date object you can grab the smaller attributes as well:
currentYear = today.year
print(f"Current Year: {currentYear}")
# Output is : Current Year: 2024

currentMonth = today.month
print(f"Current Month: {currentMonth}")
# Output is : Current Month: 6

currentDay = today.day
print(f"Current Day: {currentDay}")
# Output is : Current Day: 22

# This here is something called "ctime formatting"
print(f"today.ctime: {today.ctime()}")
# Above output is: today.ctime: Sat Jun 22 00:00:00 2024
# Databases often stores time in this format 

from datetime import datetime
myDateTime = datetime(2022, 10, 3, 14, 20, 1)
print(f"myDateTime: {myDateTime}")
# Output is: myDateTime: 2022-10-03 14:20:01
# Note it goes all the way from the largest - the year, to the smallest - the second

# We can also adjust the declaration, say we want to change 2022 to 2023:

print(f"My adjusted date time: {myDateTime.replace(year=2023)}")
# This outputs: My adjusted date time: 2023-10-03 14:20:01
# It seems like this does not actually CHANGE the original, it just outputs it with this replaced. But if you call the original again, it will be what it was 
# If you want to actually change it, you have to do it in place:
myDateTime = myDateTime.replace(year=2023)
print(f"My new datetime: {myDateTime}")
# This outputs: My new datetime: 2023-10-03 14:20:01

# One can also perform arithmatic on either a date object or a datetime object
# Date information arithmatic
# First, import date
from datetime import date

date1 = date(2023, 9, 3)
date2 = date(2022, 11, 3)

date3 = date1 - date2
print(f"difference between {date1} and {date2}: {date3}")
# Above will then figure out how much time is the difference between the 2 dates
# Difference between 2023-09-03 and 2022-11-03: 304 days, 0:00:00

# Here we are performing arithmatic on a datetime object
# You can either call dates with datetime.datetime, or say from datetime import datetime
datetime1 = datetime(2003, 4, 9, 22, 0)
datetime2 = datetime(2001, 7, 12, 17, 0)
datetime3 = datetime1 - datetime2
print(f"Difference between {datetime1} and {datetime2} is {datetime3}")
# Output here is : Difference between 2003-04-09 22:00:00 and 2001-07-12 17:00:00 is 636 days, 5:00:00



