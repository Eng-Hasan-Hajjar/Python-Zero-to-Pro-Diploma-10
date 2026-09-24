laptops = "hp,mac,acer,lenevo"
print(laptops.upper())

mobiles="iphone16PRO,redmi not 8 ,iphone,samsungS24,poco F7,iphone17PROmax"
print(mobiles.lower())

SCREENS = "   LG , SAMSUNG , TOSHIBA "
print(SCREENS)
print(SCREENS.strip()) 

print(SCREENS.replace("LG","Starway"))

print(SCREENS.replace("SAMSUNG","***"))

print(SCREENS.split(","))

print(mobiles.split(","))

food1="hamburger"
food2="cola"

full_food=food1 + " & " + food2
print(full_food)


club_year=1900
text="this club establish at : " + str(club_year) 
print(text)



price=1500
brand="iphone 18 pro max - price of it: {}"
print(brand.format(price))


quantity=3
itme_no=433
price_unit=50
myorder="I want {} peices of item {} for {} usd"
print(myorder.format(quantity,itme_no,price_unit))


quantity=6
itme_no=487
price_unit=25
myorder="I want {2} peices of item {1} for {0} usd"
print(myorder.format(quantity,itme_no,price_unit))


pharmacy="parol \"declo\" setamol"
pharmacy2="\t parol \t 'declo' \t setamol"
pharmacy3='\nparol \n"declo" \nsetamol'
print(pharmacy , pharmacy2,pharmacy3)


text = "I love Java"

print(text.replace("Java", "Python"))