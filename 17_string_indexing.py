'''credit_card = '1234-4567-8910-0012'
print(credit_card[0:4])
print(credit_card[5:9])
print(credit_card[5:])
print(credit_card[-1:])
print(credit_card[::-1])
print(credit_card[::-2])'''

# extract last four digit of credit card number
credit_num = '1234-5678-9101-1213'
credit_card = credit_num[-4:]
print(f"credit number is xxxx-xxxx-xxxx-{credit_card}")

