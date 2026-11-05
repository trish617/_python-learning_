# num1 = int(input("Enter your number :"))
# age = int(input("Enter your age : "))
# if (num1%2 ==0):
#     print("The number is even")
# if (age<=18):
#     print("you are miner")
# elif(age>18):
#     print("you are an adult")
# else:
#     print("not defined")

# # nested if else
x = int(input("Enter the value of x : "))
if (x < 100):
    print("less than 100")
elif(x > 100):
    if ((x>100) & (x<200)):
        print("between 100 and 200")
    else:
        print("Greater than 100")
else:
    print("oops!")