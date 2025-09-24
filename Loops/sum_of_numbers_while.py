# Ask the user to enter a number up to which the sum will be calculated
n = int(input("Enter the number: "))

i = 0       # Counter variable to iterate from 0 to n
sum = 0     # Variable to store the running total

# Loop until i reaches n
while i <= n:
    sum += i       # Add the current value of i to the sum
    i += 1         # Increment i by 1 to move to the next number

# Print the final sum after the loop completes
print(f"The sum of numbers till {n} is {sum}")
