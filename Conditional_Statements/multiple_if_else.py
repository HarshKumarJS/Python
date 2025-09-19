# Program to check weather conditions using multiple if and else

temperature = 30  # Current temperature in °C
rain = False      # Whether it is raining
windy = True      # Whether it is windy

# Multiple independent if statements
if temperature > 35:
    print("It's a hot day.")   # Condition 1

if rain:
    print("It's raining.")     # Condition 2

if windy:
    print("It's windy.")       # Condition 3

# Final else executes only if none of the above conditions were true
else:
    print("Weather looks normal.")
