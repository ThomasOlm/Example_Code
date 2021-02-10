## A simple class to work with calendars and return the number of weekdays in a year 

import calendar

class MyCalendar(calendar.Calendar):

    def count_weekday_in_year(self, year, day):

        counter = 0
        for months in range(1, 13):

            for data in self.monthdays2calendar(year, months):

                for tuple in data:

                    if tuple[-1] == day and tuple[0] != 0:
                        counter += 1

        return counter

c = MyCalendar()

print(c.count_weekday_in_year(2000, 6))
