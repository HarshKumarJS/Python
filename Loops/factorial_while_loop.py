# Prompt the user to enter a number
n = int(input("Enter the number: "))

factorial = 1  # Variable to store the factorial result, initialized to 1
i = 1          # Counter variable starting from 1

# Loop from 1 to n to calculate the factorial
while i <= n:
    factorial *= i  # Multiply factorial by the current number i
    i += 1          # Increment the counter by 1

# Print the final factorial of n
print(f"The factorial of {n} is {factorial}")
