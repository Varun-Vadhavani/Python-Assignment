from datetime import date
from dateutil.relativedelta import relativedelta

dob = date(2004, 10, 31)
today = date.today()

age = relativedelta(today, dob)
print(f"Your age: {age.years} years, {age.months} months, {age.days} days")