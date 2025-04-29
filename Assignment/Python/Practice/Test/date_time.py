import time

print(time.time())
print(time.localtime())
print(time.localtime().tm_mday)
print(time.strftime('%Y-%m-%d %H:%M:%S'))


import datetime as dt

today = dt.datetime.now()
 
# Attributes
print("Type of Day: ", type(today.day))
print("Type of strftime: ", type(dt.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')))
print("Day: ", today.day)
print("Month: ", today.month)
print("Year: ", today.year)
print("Hour: ", today.hour)
print("Minute: ", today.minute)
print("Second: ", today.second)

from datetime import datetime, timedelta

# Create datetime, date, and time objects
dt = datetime(2025, 4, 29, 14, 30, 0)
d = dt.date()
t = dt.time()

# Access components
print(f"Date: {d}, Time: {t}")
print(f"Year: {dt.year}, Hour: {dt.hour}")

# Arithmetic (add 1 week to datetime)
dt_plus_week = dt + timedelta(weeks=1)
print(f"One week later: {dt_plus_week}")

# Subtract two dates (difference in days)
days_diff = dt.date() - d
print(f"Days difference: {days_diff.days}")

# Formatting
formatted_dt = dt.strftime("%A, %B %d, %Y %I:%M %p")
print(f"Formatted datetime: {formatted_dt}")

# Create a datetime object
dt = datetime(2025, 4, 29, 14, 30)

# Add 5 days using timedelta
new_dt = dt + timedelta(days=5)
print(f"5 days later: {new_dt}")

# Subtract 2 days using timedelta
new_dt = dt - timedelta(hours=2)
print(f"2 days earlier: {new_dt}")

from datetime import datetime, time, timedelta

# Create a time object
t = time(14, 30)  # 2:30 PM

# Convert time to datetime (assuming a dummy date)
dt = datetime.combine(datetime.today(), t)

# Add 2 hours
new_dt = dt + timedelta(hours=2)

# Convert back to time
new_time = new_dt.time()
print(f"New time after adding 2 hours: {new_time}")


