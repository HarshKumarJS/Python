# Prompt the user to enter a number
n = int(input("Enter the number: "))

factorial = 1  # Variable to store the factorial result, initialized to 1

# Loop from 1 to n (inclusive) to calculate the factorial
for i in range(1, n + 1):
    factorial *= i  # Multiply factorial by the current number i

# Print the final factorial of n
print(f"The factorial of {n} is {factorial}")
