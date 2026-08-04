'''name = input("Enter your name : ")
result = len(name)
print(name[1])
print(name[0:6:1])'''

#name = 'trisha'
#n_name = name.capitalize()
#name_n = name.upper()
#result = name.lower()
#print(result)
#print(n_name)
#print(name_n)

'''name = 'chloe vaultz'
result = name.find('v')
result1 = name.rfind('e')
print(result)
print(result1)

text = input("Enter your text here : ")
#text1 = text.isdigit()
#print(text1)
text1 = text.isalpha()
print(text1)

# validate user input
# username is no more than 12 characters
username = input("Enter your name : ")
if len(username) > 12 :
    print("your userame cannot be more than 12 characters")
else :
    print(f"welcome {username}!")

# username must not contain any spaces
username = input("Enter your username : ")
if username.find(' ') > 0 :
    print("Usename must not contain any spaces !")
else :
    print(f"welcome {username}!")'''

# username must not contain any digits
username = input("Enter your username : ")
if username.isalpha() :
    print("Username must not contain any digits!")
else :
    print(f"hello {username}")
