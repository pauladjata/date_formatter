from date_formatter import *

date_time_string_US = "18-12-2014"
date_time_string_AUS = "12-18-2014"

myDates_US = DateFormatter.dateFormat(date_time_string_US, True, False, "US")
myDates_AUS = DateFormatter.dateFormat(date_time_string_AUS, True, False)

print(myDates_US)
print(myDates_AUS)
