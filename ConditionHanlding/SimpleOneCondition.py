# Take input from user - Number
# Check this number is Event, Print this is Even number
# Don't do anything if number is Odd
# 2,4,6,8, 122 Even Number
# 1,3,5,101 Odd Number

data = input("Please enter your number: -")
data = int(data)

if( data % 2 == 0):
    print("This is Even Number")
    print("This is my second line")
    print("End Of Condition")

print("This is Print Statement")