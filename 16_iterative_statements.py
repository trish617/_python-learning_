# #while loop statement 
start  = 1
end = 5
while (start<=end):
    print("hello pytohn")
    start += 1

# # for loop statement
name  = "Tony"
for i in name :
    if (i == 'n'):
        break
    print(i)

ch = input("Enter the string : ")
for i in ch:
    if  (i in "aeiou"):
        continue
    print(i)

my_lists = ["honey","shirt","paper"]
for i in my_lists:
    print(i)