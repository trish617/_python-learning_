from functools import reduce

list1 = [1,2,3,4,5,6]

result = (reduce(lambda  x,y : x + y , list1))
print(result)