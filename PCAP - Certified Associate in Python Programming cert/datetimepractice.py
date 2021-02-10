# Just a simple program to work with datetime and its encoded strings

import datetime

nov4 = datetime.datetime(2020, 11, 4, 14, 53, 0, 0)

print(nov4.strftime("%Y/%m/%d %H:%M:%S"))
print(nov4.strftime("%Y/%B/%d %H:%M:%S"))
print(nov4.strftime("%A, %Y, %B %d"))
print(nov4.strftime("Weekday: %w"))
print(nov4.strftime("Day of the Year: %-j"))
print(nov4.strftime("Week of the Year: %U"))
