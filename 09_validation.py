# check wether the data is integer or not
# Example 1: Using is_integer() on a simple floating - point number
a = 89
print(a.is_integer())

b = 89.90
print(b.is_integer())

#Basic Usage
#Using with Variables and Expressions
a1 = 10.00
b1 = 20.00
c = b/a
print(c.is_integer())

#user input 
user_input = float(input("enter a number : "))
print(user_input.is_integer())


# check the data type of the value
x = '123'
print(isinstance(x,int))

x = float(5)

print(isinstance(x, int))