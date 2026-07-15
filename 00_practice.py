 #Add the values 1234 and 9876 together and print the result to the screen.
num_1 = 1234
num_2 = 9876
print(num_1 + num_2)

# You received a bonus of $1,000 for your outstanding work!
#  You are planning to go to the restaurant to celebrate.
#  You invited your two best friends Alice and Bob. 
# Your dish cost $25, Alice's cost $20 and Bob's cost $30.
# How much money do you have left after dinner?
bonus_total = 1000
dish_total_cost = 75
total_remaining = bonus_total - dish_total_cost
print(total_remaining)

# Counting Squares
total_columns = 7
total_rows = 3
total_cells = total_columns * total_rows
print(total_cells)

#  use the formula to compute the body mass index of someone who weighs 66.2 kilograms
#  and has a height of 1.82 meters.Print the result to the screen.
# formula w/h2
weight = 66.2
height = 1.82
body_mass_index = weight / (height) ** 2
print(body_mass_index)

#calculate the average crime rate of five cities in united states  of America 
total_cities = 5
country_a_crime = 749
country_b_crime = 371
country_c_crime = 828
country_d_crime = 503
country_e_crime = 1379
average_crime_rate = (country_a_crime + country_b_crime + country_c_crime + country_d_crime + country_e_crime) / total_cities
print(average_crime_rate)

# Variables and Data Types Practice Problems
# Helping Alice Compute Her GPA

grade_hours = 43
total_hours = 15
gpa = grade_hours / total_hours
print(gpa) 

text = "banana"
print(text.replace("a", ""))

'''Print the first character of "DataEngineer".
Print the last character.
Print the first four characters.
Reverse "Python" using slicing.
Remove all spaces from "Hello World Python" using replace().
Count how many "a"s are in "banana".
Split "apple,banana,mango" into a list.'''

char = "DataEngineer"
print(char[0])
print(char[-1])
print(char[0:4])

word = 'Python'
print(word[::-1])

text_1 = "Hello World Python"
print(text_1.replace(" ", ""))

fruit = "banana"
print(fruit.count("a"))

fruits = "apple,banana,mango"
print(fruits.split(","))
