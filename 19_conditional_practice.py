#Accept two numbers and print the greatest between them.
'''num1 = int(input("enter the first number : "))
num2 = int(input("enter the second  number : "))
if num1 > num2 :
    print(f"{num1} is greater")
else :
    print(f"{num2} is greater")

#Accept the gender from the user as char and print the
#respective greeting message
#Ex - Good Morning Sir (on the basis of gender)

gender = input("enter your gender (M/F) : ")
if gender == 'M' :
    print("Good morning sir ")
else :
    print("Good morning Ma'am")

#Accept a year and check if it a leap year or not (google to
#find out what is a leap year)
year = int(input("Enter the year : "))
if year % 4 == 0 :
    print(f"{year} is a leap year")
else :
    print(f"{year} is not a leap year")'''

# if - elif ladder : 
t = int(input("Enter the temperature in celsius : "))
if t < 0 :
    print(" Its freezing cold")
elif t == 0 and t <= 10 :
    print("Its very cold ")
elif t > 10 and t <= 20 :
    print("Its cold")
elif t > 20 and t <= 30 :
    print("Its pleasant outside")
elif t > 30 and t <= 40 :
    print("Its hot outside")
else :
    print("Its very hot outside")