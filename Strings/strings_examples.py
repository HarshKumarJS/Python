# strings_examples.py

# Different ways to define and use strings in Python

# 1. Using single quotes
str1 = 'My name is Harsh.'

# 2. Using double quotes (useful when string contains a single quote/apostrophe)
str2 = "This is mayank's book."

# 3. Using triple single quotes ('''...''') for multi-line strings
str3 = '''I am a software developer.
My main role is backend developer.'''

# 4. Using triple double quotes ("""...""") for multi-line strings
str4 = """My hometown is Sonipat.
I am living in Gurugram as I am working there."""

# 5. Escape sequences: \n for newline
str5 = "How are you?\nAre you feeling well today?"

# 6. Escape sequences: \t for tab space
str6 = "Today, I am very busy.\tTold someone else to do this."

# 7. Raw strings: r"..." -> escape sequences are ignored
raw_str = r"C:\Users\Harsh\Documents"
# Without raw string -> "C:\n" would be treated as a newline

# 8. Unicode strings (default in Python 3)
uni_str = "नमस्ते"  # Hindi
uni_str2 = "こんにちは"  # Japanese

# 9. Byte strings: b"..." -> stores data in bytes
byte_str = b"Hello"
# Useful for low-level operations like networking or file handling in binary mode


# Printing all string examples

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(raw_str)
print(uni_str)
print(uni_str2)
print(byte_str)
