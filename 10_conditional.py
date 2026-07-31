age = int(input("enter yor age : "))
if age>=100 :
    print("you are too old to vote!")
elif age>=18 :
    print("you are eligible for vote!")
else :
    print("not eligible for vote!")    

#if a coustomer want food 
response = str(input("would you like to order your food ? "))
if response == 'yes' :
    print("list your oerder! ")
elif response == 'maybe' :
    print("we appreciate you looked!")
else :
    print("thank you for stopping by!")    

#simple calculator 

operator  =(input("enter the operator : "))
num1 = float(input("enter the first number : "))
num2  = float(input("enter the second number : "))

if operator == "+" :
    result = num1 + num2
    print(round(result,2))
elif operator == "-" :    
    result = num1 - num2
    print(round(result,2))
elif operator == "*" :
    result = num1 * num2
    result = num1 * num2
    print(round(result,2))     
elif operator == "/" :
    result = num1 / num2
    print(round(result,2))
else :
    print(f"{operator} is not a valid operator")

