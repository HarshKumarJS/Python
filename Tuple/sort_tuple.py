# Program to sort a tuple in ascending order using two methods

# Original tuple
t = ('C', 'D', 'A', 'A', 'B', 'B', 'A')

# -------------------- Method 1: Using list conversion and sort() --------------------
# Convert tuple to list
l = list(t)
# Sort the list in-place
l.sort()
# Convert back to tuple
sorted_tuple1 = tuple(l)
print(f"Sorted tuple using list conversion and sort(): {sorted_tuple1}")

# -------------------- Method 2: Using sorted() --------------------
# sorted() returns a new sorted list, convert it to tuple
sorted_tuple2 = tuple(sorted(t))
print(f"Sorted tuple using sorted(): {sorted_tuple2}")
