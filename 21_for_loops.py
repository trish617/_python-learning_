# practice questions
#Accept an integer and Print hello world n times
n = int(input("Enter an integer : "))
for i in range(n) :
    print("hello world")

#Print natural number up to n
n = int(input("Enter the number :"))
for i in range(0,n+1) :
    print(i)

#Reverse for loop. Print n to 1
n = int(input("Enter your number : "))
for i in range(n,0,-1) :
    print(i)   

#Take a number as input and print its table
n = int(input("Enter the number for table you want : "))
for i in range(1,11) :
    print(f"{n} * {i} = {n*i}")