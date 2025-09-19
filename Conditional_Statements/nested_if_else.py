# Program to check voting eligibility using nested if-else

age = 20          # Age of the person
nationality = "Indian"  # Nationality of the person

# First check if the person is old enough
if age >= 18:
    # Nested if: check nationality only if age condition is satisfied
    if nationality == "Indian":
        print("Eligible to vote in India.")  # Age >= 18 and Indian
    else:
        print("Not eligible to vote in India.")  # Age ok but nationality not Indian
else:
    print("Not eligible to vote.")  # Age less than 18
