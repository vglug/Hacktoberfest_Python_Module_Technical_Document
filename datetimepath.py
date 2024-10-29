import datetime

# Get current date and time
now = datetime.datetime.now()

# Print the current date and time
print("Current date and time:", now)
Extract components of the current date and time
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second

# Print the components of the current date and time
print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Hour:", hour)
print("Minute:", minute)
print("Second:", second)

