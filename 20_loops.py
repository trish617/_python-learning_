#for loop
a = range(1,21,2)
for i in a :
    print(f"this is odd number : {i}")

# Accept an integer and Print hello world n times
numb = int(input("Enter your number : "))
for i in range(1,numb,1) :
    print("hello wprld")

# reverse loop
for i in range(100,81,-1) :
    print(i)

# print table of 5
for i in range(5,51,5) :
    print(i)
n = int(input("Which table  do you want : "))
for i in range(n,(n*10)+1,n) :
    print(i)

# for loops with strings 
a  = "ROBERT"
for i in range(6) :
    print(a[i])

b = "CALEB CURRY WITHMORE"
for i in range(len(b)) :
    print(b[i])

a = "Hello world"
for i in a :
    print(i)

for i in range(1,16) :
    if i == 10 :
        break
    else :
        print(i)

for i in range(1,16) :
    if i == 10 :
        continue
    else :
        print(i)
for i in range(0,21) :
    if i == 14 :
        print("break statement executed")
        break
    print(i)
else :
    print("break statement does not executed")


 