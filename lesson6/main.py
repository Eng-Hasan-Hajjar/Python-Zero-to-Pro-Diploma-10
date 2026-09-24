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


number = "25"

print(number.zfill(5))

##yasamin
text = "السعر ١٢٥ ليرة"

table = str.maketrans(
    "٠١٢٣٤٥٦٧٨٩س",
    "0123456789s"
)

result = text.translate(table)
print(text)
print(result)


#magd
text="pytHOn programming"
print(text.capitalize())  # Python
print(text.title())       # Python Programming
print(text.swapcase())    # صغير ↔️ كبير

#kinda
students = {}

students.setdefault("Ali", []).append("Python")
students.setdefault("Ali", []).append("Java")
students.setdefault("Omar", []).append("C++")
students.setdefault("Ali", []).append("C++")
students.setdefault("Eric", []).append("python")
students.setdefault("Eric", []).append("math")
print(students)




filename = "photo.jpg"

if filename.startswith("photo"):
    print("هذه صورة")
if filename.endswith("jpg"):
    print("this nice ")    
    
#zahraa
countries = "Syria-Italy-France-Spain"
all_countries = countries.split("-")
print(all_countries)
first_split = countries.split("-", 1)
print(first_split)


#eric
prices = [20, 100, 50, 200, 30]
cheap = list(filter(lambda price: price < 100, prices))

print(cheap)

#zahra
text = "hello world"

position = text.rfind("o")
position = text.find("o")

print(position)


