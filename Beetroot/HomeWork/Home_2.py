from datetime import date
from datetime import datetime
import os

print('Home work 2.1')
week_day = date.weekday(datetime.now())
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
print('Good day ' + os.getlogin().title() + '! ' + days[week_day].title() + ' is a perfect day to learn some python.')

print('\nHome work 2.2')
name = "Evhenii"
sur_name = "Serbul"
print("Hello " + name + " " + sur_name + "!")

print("")
print('Home work 2.3')
a = 25
b = 10

print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(a ** b)
print(a % b)
print(a // b)
