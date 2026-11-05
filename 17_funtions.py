# creating a funtion and passing parameters and arguments 
def my_func(x): #passing parameters
    if(x > 10):
        print("greater than 10")
    else:
        print("not greater than 10")

    return x    
return_value = my_func(x = 50) #passong an argumnet thats is the value 
print(return_value)

# def number(*x): #accept multiple positional arguments

# print(*x,type(x))

    
# number(10,20,30,50)

#lambda funtion
addition = lambda a,b : a+b 
val = addition(100,120)
print(val)

#map 
lists1 = [1,2,3,4,5]
result = list(map(lambda l : l + 5, lists1))
print(result)

#filter 
my_lists = [1,2,3,4,5]
newl = list(filter(lambda l : l %2 == 0,my_lists))
print(newl)

num = [1,2,3,4,5,6]
def even_odd (n):
    if n % 2 == 0:
        return n

number = list(filter(even_odd,num))
print(number)


 


