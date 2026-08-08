# a = 1
while a <= 15 :
    print("hello world")
    a += 1

# Separate each digit of a number and print it on the new line
a = 7922
while a > 0 :
    print(a % 10)
    a = a // 10

# Accept a number and print its reverse
n = int(input("Enter the number : "))
reverse = 0
while n > 0 :
    reverse = reverse * 10 + n % 10
    n = n // 10
print(reverse)