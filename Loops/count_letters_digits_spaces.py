# This script counts the number of letters, digits, and spaces in a given string.

# string to analyze
a = "harshsrt 9220 rathee"

# Initialize counters for letters, digits, and spaces
letters = 0
digits = 0
spaces = 0

# Loop through each character in the string
for i in a:
    if i.isalpha():        # Check if the character is an alphabet (A-Z or a-z)
        letters += 1       # Increment the letter counter
    elif i.isdigit():      # Check if the character is a digit (0-9)
        digits += 1        # Increment the digit counter
    elif i.isspace():      # Check if the character is a whitespace
        spaces += 1        # Increment the space counter

# Display the results
print(f"Letters = {letters}, Digits = {digits}, Spaces = {spaces}")
