# Program to check if a list contains a palindrome of elements

# Sample list
l = [1, 'abc', 'abc', 1]

# Check if the list is equal to its reverse
if l == l[::-1]:
    print("Yes, the list is a palindrome")
else:
    print("No, the list is not a palindrome")
