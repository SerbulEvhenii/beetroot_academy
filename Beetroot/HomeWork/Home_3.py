print("Home work 3.1")
input_string = str(input())
if len(input_string) < 2:
    print('Empty string')
elif len(input_string) == 2:
    print(input_string * 2)
else:
    print(input_string[0:2] + input_string[-2:])

print("\nHome work 3.2")
phone_number = "0636038567"
if phone_number.isdecimal() and len(str(phone_number)) <= 10:
    print("Phone number entered correctly")
else:
    print("Phone number entered incorrectly. Repeat one more time")


print("\nHome work 3.4")
user_name = 'Evhenii'
input_user_name = str(input())
if input_user_name.lower() == user_name.lower():
    print('Entry allowed')
else:
    print('You entered an invalid username')
