# Python Ver:   3.5
#
# Author:       Justin Tolson
#
# Purpose:      Create code that will use the current time of the Portland HQ to find out the time in the NYC &
#                London branches, then compare that time with the branches hours to see if they are open or
#               closed.
#               Print out if each of the two branches are open or closed.
#
#
# import the datetime library

import datetime

# establish my main object class

class Location(object):

    # establish my hours of operation

    opening_hour = 9
    closing_hour = opening_hour + 12

    # initialize my two parameters that I will be using

    def __init__(self, branch, timezone=0):
        self.branch = branch
        self.timezone = timezone

    # establish what I want to view when locations are printed

    def __str__(self):
        return self.branch + " branch is " + self.displayTime() + "."

    # determines whether the location is open or closed depending on hours of timezone compared to hours of operation

    def displayTime(self):

        now = datetime.datetime.utcnow()

        time_in_timezone = now.hour + self.timezone

        if self.opening_hour <= time_in_timezone <= self.closing_hour:
            return "open"
        else:
            return "closed"

# print and label what the current time is

timeNow = datetime.datetime.now()
print("Your current time is " + timeNow.strftime('%H:%M') + ".\n")

# established a list of locations to be looped through

locations = [
    Location('Portland', -8),
    Location('New York', -5),
    Location('London', 0)

]

# for loop to start the program

for Location in locations:
    print(Location)