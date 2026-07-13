#string function types(type() & str())
age = 24
print(type(age))
print("your age is:",age)
print("your age is:" + str(age))

#string function maths (len() & count())

password = '  risha123' # count spaces also
print(len(password))

notice = """
            hi everyone. i hope you are doing well. 
            you are requested to come tomorrow.
         """
print(notice.count("you"))

#string function transformation 
# text.replace("old","new")
# challenge use replace()
phone = "+49(176) 123-4567"
print(phone.replace("+","").replace("(","").replace(")","").replace(" ","").replace("-",""))

#+ operator 'string'+'string'
destination = "Thailand"
money_spent = "80000"
info_total = destination  + " - " +  money_spent
print(info_total + " " + "total spent")

#data transformation f-string
name1 = "chloe"
age1 = 26
print(f"my name is {name1}. i am {age1} years old")