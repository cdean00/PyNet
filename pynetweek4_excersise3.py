"""
Week 4, Excersise 3
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
III. Create a program that converts the following uptime strings to a time in seconds.

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'

uptime2 = '3750RJ uptime is 1 hour, 29 minutes'

uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'

uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'



For each of these strings store the uptime in a dictionary using the device name as the key.

During this conversion process, you will have to convert strings to integers.  For these string to integer conversions use try/except to catch any string to integer conversion exceptions.



For example:

int('5') works fine

int('5 years') generates a ValueError exception.



Print the dictionary to standard output.
"""

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

uptime1_weeks = uptime1[uptime1.find("weeks")-2]
uptime1_days = uptime1[uptime1.find("days")-2]