attendence = int(input("enter the percentage of attendence:"))

if attendence < 75:
    print("you have failed to meet the attendence requirement to be promoted to the next grade")
else:
    print("your attendence meets the requirements to be promoted to the next grade")

import datetime
#using now() to get current time
current_time = datetime.datetime.now()

print("time now at greenwich median is:",end="")
print(current_time)

#print calender of year 2025
import calender
print("\n", calender.calender(2025))