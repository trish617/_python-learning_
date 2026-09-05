#A tuple is an immutable data type in python.
a = () # empty tuple
a = (1,) # tuple with only one element needs a comma
a = (1,7,2) # tuple with more than one element
print(a) 

# tuple methods
# 1. count()
# count() tells us how many times a value appears in a tuple.

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))

# 2. index()
# index() tells us the position of the first occurrence of a value.

fruits = ("apple", "banana", "kiwi", "banana")

print(fruits.index("banana"))