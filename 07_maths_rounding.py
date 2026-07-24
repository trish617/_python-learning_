import math
# abs()
point_a  = 25
point_b = 10
distance = point_a - point_b
print(distance)

point_a  = 25
point_b = 30
print(abs(point_a - point_b)) # we get absolute value

# round()
a = 2.7
print(round(a))

b = 2.4
print(round(b))

#floor()
c = 2.4
print(math.floor(c))

#ceil()
c = 2.4
print(math.ceil(c))

# round half to even
ditance_2 = 35.559687
print(round(ditance_2,2))

# trunc()
ditance_2 = 35.559687 # dont want any decimal part
print(math.trunc(ditance_2)) 

#power
abc = pow(10,10)
print(abc)

# maximum value
a = 40
b = 30
c = 10
abc1 = max(a,b,c)
print(abc1)
abc2 = min(a,b,c)
print(abc2)

# exercise = calculate the circumference of a circle
'''pi = 3.14
r = 20
circumference = 2*pi*r
print(circumference)'''

# calculate through userinput
pi = 3.14
radius = float(input("enter the radius of circle : "))
circumference = 2*pi*radius
print(f"circumference of the circle is {round(circumference,2)}")

#calculate the area of a circle
r = float(input("enter the radius of a circle : "))
area = math.pi * pow(r , 2)
print(f"area of a circle is {round(area , 2)} cm\u00B2")

#calculate the hypotenuse of an right angled triangle
base = float(input("enter the base of right angle triangle : "))
height = float(input("enter the height of right angle triangle : "))
hypotenuse = pow(base , 2) + pow(height , 2)
print(f"hypotenuse of right angle triangle = {round(hypotenuse , 2)} cm\u00B2")