# VARIABLES
# sum of numbers from 1 to n
n1 = float(input("enter first number : "))
n2 = float(input("enter second number : "))
sum = n1 + n2
print(f"sum of the two numbers are {sum}")

# Take two integers from the user and print their sum.
int1 = float(input("enter the first number : "))
int2 = float(input("enter the second number : "))
sum = int1 + int2
print(f"sum of two integer is {sum}") 

# Swap two variables without using a third variable.
a = 10 
b = 20
a,b = b,a
print(f"value of a is {a}")
print(f"value of b is {b}")

#Store your height in centimeters and print it in meters.
height = float(190)
new_height = height / 100
print(f"height is {new_height}m")

# Create variables python_marks, sql_marks, java_marks and print the total
python_marks = 89
sql_marks = 92 
java_marks = 95
total = python_marks + sql_marks + sql_marks
print(f"Total marks = {total}")

# TYPECASTING
# Take age as input and convert it to int
age = input("enter your age : ")
age = int(age)
print(f"Your age is {age}")

# Take price as input and convert it to float
price = (input("enter the price : "))
price = float(price)
print(f"The price is {price}")

# Convert integer 25 to string and print "Age: 25"
age = 25
age = str(age)
print(f"Age : {age}")

# Convert float 7.9 to integer and print the resul
num = 7.9
num = int(num)
print(num)

# ARITHMETIC OPEARTORS
# Divide two numbers and print quotient
a = 5
b = 3
c = a / b
print(round(c,2))

# Find remainder when one number is divided by another
a = 19
b = 2
remain = a % b 
print(round(remain, 2))

# Comparison Operators
# Check whether two numbers are equal
num1 = 20
num2 = 20
print(num1 == num2)

# Take age and check whether it is at least 18
age = int(input("enter your age : "))
print(age >= 18)

# Logical Operators
# Check whether a number is between 10 and 20 using and
num = int(input("enter a number : "))
print(num > 10 and num <= 20)

# Check whether a number is divisible by both 3 and 5
num = 15 
print(num % 3 == 0 and num % 5 == 0)

# Check whether a character is a vowel using or
ch = input("enter a character : ")
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' :
    print(f"The character {ch} is an vowel")
else :
    print(f"The character {ch} is a consonant")

# Check whether a student passed if marks are above 40 and attendance above 75
marks = float(input("Enter the total marks : "))
attendance = float(input("Enter total no of attendace : "))
if marks >= 40 and attendance >= 75 :
    print("Passed!")
else :
    print("Failed!")

# Use not to check whether a number is not positive
num = -10
if not (num > 0) :
    print("Number is not positive")
else :
    print("Number is positive")

# CONDITIONAL STATEMENT
# Positive / negative / zero
num = int(input("enter a number : "))
if num >= 0 :
    print("The number is positive")
else :
    print("The number is negative")

num = int(input("Enter a number : "))
if num == 0 :
    print("Zero")
else :
    print("Non zero")

# Largest of two numbers
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if num1 > num2 :
    print(f"Largest is {num1}")
else :
    print(f"Largest is {num2}")
    







