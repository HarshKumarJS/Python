# Ask user to enter a number
n = int(input("Enter the number: "))

i = 1  # Initialize the counter
while i <= 10:
    product = i * n  # Calculate the product of n and the current multiplier
    # Display the multiplication in the format: n * i = product
    print(f"{n} * {i} = {product}")
    i += 1  # Increment the counter