""" bro 
  YT code"""
# 1 . python weight converter

# weight = float(input("Enter your weight : "))
# unit = input("Killograms or pounds ( K or P ): ").strip().title()

# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs"
#     print(f"Your weight is: {round(weight , 1)} {unit}")

# elif unit == "P":
#     weight = weight / 2.205
#     unit = "Kgs"
#     print(f"Your weight is: {round(weight , 1)} {unit}")

# else:
#     print(f"{unit} was not valid ")


# 2.  temperature conversion program

# unit = input("Is this temperature is celcius or fahrenheit (C/F):").title()
# temp = float(input("Enter the temperature : "))

# if unit == "C":
#     temp = round(( 9 * temp) / 5 + 32 , 1)
#     print(f"The temperature in fahrenheit is: {temp}°F")

# elif unit == "F":
#     temp = round((temp - 32 ) * 5 / 9  , 1)
#     print(f"The temperature in celcius is: {temp}°C")

# else :
#     print(f"{unit} is an invalid unit of measurement")


# 03 :  countdown timer program

# import time

# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)

#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("TIME'S UP ")


# 4 : shoping cart program

food = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy ( q to Quite): ")
    if food.lower() == "q":
        break

    else:
        price = float(input(f"Enter the price of a {food}: $"))
        food.append(food)
        prices.append(price)

print("----- Your Cart -----\n")

for food in food:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is :${total}\n")

 
# 5:
