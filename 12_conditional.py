 #Write a program to print the age entered by the user 
a = int(input("enter your age : "))
if (a>10 and a<=17) :
    print("you are teen")
elif (a == 18 and a <= 99) :
    print("you are eligible")
else :
    print("you are not eligible")

#nested if statememt : if --elif---else inside another if--elif--else statement
hungry = True
money = 100
restaurantOpen = True
if(hungry) :
    if(money == 0):
        print("just sleep")
    elif(money<500):
        print("have something nice")
    elif(money>1000):
        print("have a party")
    else:
        print("just order in ")

else:
    print("sleep")


