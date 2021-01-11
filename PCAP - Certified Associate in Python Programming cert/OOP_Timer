## A program to create a timer that can be updated by increasing or decreasing the seconds 

class Timer:
    
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        #
        # Write code here
        #
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        #
        # Write code here
        #

        str_hours = str(self.hours)
        str_mins = str(self.minutes)
        str_secs = str(self.seconds)

        if self.hours < 10:
            str_hours = "0" + str(self.hours)

        if self.minutes < 10:
            str_mins = "0" + str(self.minutes)

        if self.seconds < 10:
            str_secs = "0" + str(self.seconds)

        output_string = str_hours + ":" + str_mins + ":" + str_secs

        return output_string

    def next_second(self):
        #
        # Write code here
        #

        if self.seconds + 1 == 60:

            self.seconds = 0

            if self.minutes + 1 == 60:

                self.minutes = 0

                if self.hours + 1 == 24:

                    self.hours = 0

        else:
            self.seconds += 1


    def prev_second(self):
        #
        # Write code here
        #

        if self.seconds - 1 == -1:

            self.seconds = 59

            if self.minutes - 1 == -1:

                self.minutes = 59

                if self.hours - 1 == -1:
                    self.hours = 23

        else:
            self.seconds -= 1


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
