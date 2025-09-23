# This program searches for a number in a list.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 81  # Number to search for
index = 0

for i in a:
    if i == x:
        print(f"Your number {x} is at index {index}")  # Number found
        break
    index += 1
else:
    # Executed only if the for loop is not broken (number not found)
    print(f"Your number {x} is not in the list")
