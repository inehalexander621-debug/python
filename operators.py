# Concatenation: Joining two or more strings using the + operator.
s1 = "Hello"
s2 = "World"
combined = s1 + " " + s2  # "Hello World"
print(combined)

# Repetition: Repeating a string multiple times using the * operator.
repeated = "abcqwertyujhgfd" * 3  # "abcabcabc"
print(repeated)

# Indexing: Accessing individual characters by their position (index), starting from 0. Negative indices count from the end.
text = "Python"
first_char = text[0]  # 'P'
last_char = text[-2]  # 'n'
print(text[3] + text[5] + last_char)

# Slicing: Extracting a substring (a portion of the string) using [start:end:step].
text2 = "Programming your bag"
sub = text2[3:7]  # "Prog"
rev = text2[::-1]  # "gnimmargorP"
print(sub)
print(rev)

# Membership Testing: Checking if a substring exists within a string using the in or not in operators.
sentence = "Python is fun2"
is_present = " is fu" in sentence  # True
print(is_present)

# String Formatting: Creating formatted strings using f-strings (formatted string literals), str.format(), or the % operator. F-strings are generally preferred in modern Python.
name = "ALlice EGGugu"
age = 30
formatted_str = f"Name: {name}, Age: {age}"
print(formatted_str)

# Case Conversion:
# upper(): Converts to uppercase.
# lower(): Converts to lowercase.
# capitalize(): Capitalizes the first character.
# title(): Capitalizes the first letter of each word.
# swapcase(): Swaps uppercase to lowercase and vice-versa.

upPer = name.upper()
lowerCase = name.lower()
capitalize = name.capitalize()
swapcase = name.swapcase()
print(upPer)
print(lowerCase)
print(capitalize)
print(swapcase)

# Searching and Replacing:
# find(substring): Returns the lowest index of the substring, or -1 if not found.
# rfind(substring): Returns the highest index of the substring, or -1 if not found.
# index(substring): Similar to find(), but raises a ValueError if the substring is not found.
# replace(old, new): Replaces all occurrences of old with new.
# startswith(prefix): Checks if the string starts with a given prefix.
# endswith(suffix): Checks if the string ends with a given suffix.

my_string = "helloworld,I am Ogogi "
index = my_string.rfind("rl")
index2 = my_string.index("orl")
findReplace = my_string.replace("orld", "itney")
checkPrefix = my_string.startswith("ell")
checkSuffix = my_string.endswith("ld")
splitDelimiter = my_string.split(",")
print(splitDelimiter)
print(index)
print(index2)
print(findReplace)
print(checkPrefix)
print(checkSuffix)

# Whitespace and Character Manipulation:
# strip(): Removes leading and trailing whitespace.
# lstrip(): Removes leading whitespace.
# rstrip(): Removes trailing whitespace.
# split(delimiter): Splits the string into a list of substrings based on a delimiter.
# join(iterable): Joins elements of an iterable (e.g., list of strings) into a single string using the string as a separator.

stripLetter = my_string.strip()
lstStripLetter = my_string.lstrip()
rstripLetter = my_string.rstrip()
print(stripLetter)
print(lstStripLetter)
print(rstripLetter)

# Joining a list of strings with a space as a separator
words = ["Hello", "world", "from", "Python"]
result_string = " ".join(words)
print(result_string)

# Joining a list of strings with a comma and space as a separator
fruits = ["apple", "banana", "cherry"]
result_string_2 = ", ".join(fruits)
print(result_string_2)

# Joining characters of a string with a hyphen as a separator
my_string = "PYTHON"
result_string_3 = "-".join(my_string)
print(result_string_3)

# Attempting to join an iterable containing non-string elements will raise a TypeError
numbers = ["one", 2, "three"]
try:
    ",".join(numbers)
except TypeError as e:
    print(f"Error: {e}")
