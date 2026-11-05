# file handling 
# open mode = 'r','w','a'

# read mode
with open('example.txt','r') as file:
    content = file.read() # read entire content # to open a file
print(content) 
file.close()

file  = open('example.txt','r') # to open a file
content = file.readline() # read entire content
print(content) 
file.close()

file  = open('example.txt','r') # to open a file
content = file.readlines() # read entire content
print(content) 
file.close()

# write mode
with open('example1.txt','w') as file :
    file.write("welcome to another text file!\n")

# append mode

with open('example.txt','a') as file :
    file.write("welcome to another text file!\n")









