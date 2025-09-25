# Ask user to enter a number
n = int(input("Enter the number: "))

sum = 0  # Variable to store the running total

# Loop from 0 to n (inclusive) to calculate the sum
for i in range(0, n + 1):
    sum += i  # Add the current value of i to the sum

# Print the final sum after the loop completes
print(f"The sum of numbers till {n} is {sum}")
