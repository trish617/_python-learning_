# Write a python program to display a user entered name followed by Good Afternoon using
# input() function
name = input("Enter your name : ")
print(f"Good afternoon {name}")

# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
template = '''
 Dear <|Name|>,
 You are selected!
 <|Date|>
 '''
letter = template.replace("<","").replace(">","").replace("|","").replace("Name","Richard").replace("Date","24th sept")
print(letter)


