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