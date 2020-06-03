"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html
Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.
This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""
# These are modules
import sys 
import calendar
from datetime import datetime

# starts the week on a Monday displays the week headers
# The number represents how many letters to display
print(calendar.weekheader(3))
print() # adds a space in your output

# prints the index of the first weekday which is 0
print(calendar.firstweekday())
print()

# prints the selected month (1-12) and the given year
print(calendar.month(2020, 3,))
print()

# prints out the calendar in a flat list 
print(calendar.monthcalendar(2020, 3))
print()



# prints out the calendar for the entire year
print(calendar.calendar(2020))
print()

# prints out the corresponding integer to the day of the week: Monday = 0
day_of_the_week = calendar.weekday(2020, 5, 8)
print(day_of_the_week)
print()

# prints out if a year is a leap-year
is_leap = calendar.isleap(2020)
print(is_leap)
print()

# prints out how many leap-days over the span of years
# it is exclusive and leaves out the given year
how_many_leap_days = calendar.leapdays(2000, 2021)
print(how_many_leap_days)
print()

args = sys.argv
now = datetime.now()
month = now.month
year = now.year
# the given initial argument
if(len(args) == 1):
     pass

# user inputs one argument
elif(len(args) == 2):
     month = int(args[1])
     
elif(len(args) == 3):
    month = int(args[1])
    year = int(args[2])
else:
     print("wrong format")
     

if month < 1 or month > 12:
     print("error: Invalid month")
     

tc = calendar.TextCalendar()
tc.prmonth(year, month)