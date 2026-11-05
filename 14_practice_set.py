# Write a program to find the greatest of four numbers entered by the user
a = int(input("Ënter your number : "))
b = int(input("Ënter your number : "))
c = int(input("Ënter your number : "))
d = int(input("Ënter your number : "))
if (a > b and a> c and a > d):
    print(f"{a} is grater")
elif(b>a and b>c and b>d):
    print(f"{b} is greater")
elif(c > a and c > b and c >d):
    print(f"{c} is greater")
else:
    print(f"{d} is greater")

''' Write a program to find out whether a student has passed or failed if it requires a total of
40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
input from the user'''

marks1 = int(input("Enter your marks of sub1 : "))
marks2 = int(input("Enter your marks of sub2 : "))
marks3 = int(input("Enter your marks of sub3 : "))

# check for the total percentage
total_percentage = (100)*(marks1 + marks2 + marks3) / (300)

if (total_percentage >= 40):
    print("you are pass")
else:
    print("you are failed")

