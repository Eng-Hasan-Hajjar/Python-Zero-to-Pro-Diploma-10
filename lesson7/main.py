#functions of string


name="eric"
new_name=name.capitalize()
print(name, new_name)

name="ZAHRAA"

new_name=name.casefold()

new_name2=new_name.capitalize()

print(name,new_name, new_name2)

name="ZAHRAA"
print(name.capitalize())

##center
drinks="coffee"
text=drinks.center(20)
print(drinks)
print(text)



drinks="nescafeh"
text=drinks.center(20,"*")
print(drinks)
print(text)


##count()
deplams="c++,c#,python,ruby,html,css,js,python"
n=deplams.count("python")
print(n)


deplams="c++,c#,python,ruby,html,css,js,python"
n=deplams.count("python",0,10)
print(n)

deplams="c++,c#,python,ruby,html,css,js,python"
n=deplams.find("python")
print(n)


deplams="c++,c#,python,ruby,html,css,js,python"
n=deplams.find("h")
print(n)


deplams="c++,c#,python,ruby,html,css,js,python"
n=deplams.find("h",12,30)
print(n)


deplams="c++,c#,python,ruby,html,css,js,python"
n=deplams.find("z")
print(n)


##index
#deplams="c++,c#,python,ruby,html,css,js,python"
#n=deplams.index("z")
#print(n)

##isalnum
number="Hayma 😎 ***"
print(number.isalnum())
print(number.isalpha())
print(number.isascii())

number="963852741"
print(number.isdigit())
number="9.5"
print(number.isdecimal())

products="sugar,water And,milk"
print(products.islower())


products="sugar,water and,milk 1234564"
print(products.islower())

## join
products=("sugar","water" ,"milk")
all_products=" & ".join(products)
print(all_products)



products=["sugar","water" ,"milk"]
all_products=" & ".join(products)
print(all_products)

##partition

products="sugar,water,milk"
b=products.partition(",")
print(b)


products="sugar,water,milk"
b=products.partition("water")
print(b)

products="sugar,water,milk"
b=products.partition("milk")
print(b)


products="sugar,water,milk"
b=products.partition("sugar")
print(b)


