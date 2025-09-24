# Ask user to enter a number
n = int(input("Enter the number: "))

# Loop from 1 to 10 (inclusive) to print the multiplication table
for i in range(1, 11):
    product = n * i  # Calculate the product of n and the current multiplier
    # Display the multiplication in the format: n * i = product
    print(f"{n} * {i} = {product}")
