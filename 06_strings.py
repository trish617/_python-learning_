"""Strings
String is a data type in python.
String is a sequence of characters enclosed in quotes"""

# name = "Rihana" # strings in a double quotes
# name = 'Rihana' # strings in a single quotes
# name = '''Rihana''' # strings in a triple quotes 

# string slicing
# A string in python can be sliced for getting a part of the strings

name = "Rosie"
name_short = name[0:3]
name_short = name[::-1] #reversing the order 
name_short = name[::2] #slicing with skip value 
print(name_short)

# string functions

# length ()  returns the length of the string
name = "Cipher"
new = len(name)
print(new)

# endswith() checks if a string ends with given text
name = "Tommy"
print(name.endswith("ty"))

# count() counts total occurrences of a character
name = "Tommy"
print(name.count("m"))

# capitalize() capitalizes the first character
name = "tira"
print(name.capitalize())
str = "harry"
capitalized = str.capitalize()
print(capitalized) 

# replace(old word, new word) replaces the old word with the new word in the string
ph_no = "123-456-7890" # i want only the numbers 
new = ph_no.replace("-","") # replaced the old value with the new one 
print(new)

# 1. strip()
name = "  Richard  "
print(name.strip())


# 2. lstrip()
name = "  Richard"
print(name.lstrip())


# 3. rstrip()
name = "Richard  "
print(name.rstrip())


# 4. lower()
name = "Richard"
print(name.lower())


# 5. upper()
name = "tRichard"
print(name.upper())

# 7. split()
text = "I like Python"
print(text.split())


# 8. join()
words = ["I", "like", "Python"]
print(" ".join(words))




