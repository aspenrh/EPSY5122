# EPSY 5122
# IN-CLASS CHALLENGE
# 10/5/2022

def weather(temp):
    if temp >= 75:
        print("It's supposed to be Fall now!")
        return (temp - 32)/1.8
    elif temp > 60:
        print("It's not quite Halloween time!")
    else:
        print("Halloween time!")
        return (temp-32)/1.8

weather(100)
weather(76)
weather(75)
weather(74)
weather(9)
weather(-40)
weather('eighty')
weather([77, 70])
