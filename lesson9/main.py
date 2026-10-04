##operators
##+

like=0
like=like + 1

print(like)


like=0
like=like + 10
like=like - 1
print(like)

order_price = 27
discount = 5

final_price = order_price - discount

print(final_price)

"""
daily_salary=float(input("enter your daily salary: "))
num_days=float(input("enter your num days: "))
salary=daily_salary * num_days
print(salary)
"""


#monnth_salary=float(input("enter your manth salary: "))
#daily_salary=monnth_salary / 28
#print(daily_salary)


monnth_salary=float(input("enter your manth salary: "))
daily_salary=monnth_salary % 3
print(daily_salary)



x= 3 ** 2
print(x)

x= 10 / 3
print(x)
x= 10 // 3
print(x)


y=5
h=3
print(y>h)
print(y<h)
print(y>=h)
print(y<=h)

print(y==h)
print(y!=h)


age=18
amount=4800
print(age>=18 and amount>3500)



num_ex=5
num_ex2=3
print(num_ex>2  or num_ex2 > 6)
print(not(num_ex>2  or num_ex2 > 6))



x=2
y=3

print(x ^ y)
