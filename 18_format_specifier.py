# format specifier 
price1 = 4500.8936
price2 = 96000
price3 = 3.149865
print(f"price 1 is ${price1:^,.2f}")
print(f"price 2 is ${price2:^,.2f}")
print(f"price 3 is ${price3:^,.2f}")

salary = 45678.987
city = "Mumbai"
ratio = 0.7345

# Print salary with comma and 2 decimals
# Print city centered in width 20
# Print ratio as percentage with 2 decimals

print(f"salary is {salary:,.2f}")
print(f"city = {city:^20}")
print(f"ratio is {ratio:.2%}")