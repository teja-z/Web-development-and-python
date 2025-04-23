import pandas as pd
from datetime import datetime, date, time

# a) Date time object for Jan 15, 2012
a = pd.to_datetime("2012-01-15")
print("a) Date time object for Jan 15, 2012:", a)

# b) Specific date and time of 9:20 PM
b = pd.to_datetime("2012-01-15 21:20")
print("b) Specific date and time of 9:20 PM:", b)

# c) Local date and time (current system local datetime)
c = pd.Timestamp.now()
print("c) Local date and time:", c)

# d) A date without time
d = pd.to_datetime("2025-04-10").date()
print("d) A date without time:", d)

# e) Current date
e = date.today()
print("e) Current date:", e)

# f) Time from a date time
f_datetime = pd.to_datetime("2025-04-10 18:45:30")
f = f_datetime.time()
print("f) Time from a date time:", f)

# g) Current local time
g = datetime.now().time()
print("g) Current local time:", g)
