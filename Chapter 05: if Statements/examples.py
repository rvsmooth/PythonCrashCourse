# print bmw in all caps when using the for loop using if
cars = ["audi", "bmw", "subaru", "toyota", "mercedes"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car)

# Conditional Tests
# At the very heart of every if statement is an expression that can
# be evaluated as True or False and is called a conditional test
# python uses the values True or False to proceed with the statements
# provided in the if block
# in essence python executes the statements under if block
# if the conditoonal test returns True

# Checking for equality
# '==' : sign for checking equality
# >>> car == 'bmw'
# True or False
# '=' : assigning a variable

# ignore case when checking for equality

car = "Tata"

if car.lower() == "tata":
    print("So yeah you are using tata")

# Checking for Inequality
requested_car = "Toyota"

if requested_car != "tata":
    print("it ain't tata mate")
# or
if not requested_car == "tata":
    print("it still ain't tata mate")

# Numerical Comparisons
age = 18
if age == 18:
    print("You are an adult at", age)

age = 17
if age != 18:
    print("You are not an adult at", age)

age = 20
if age > 18:
    print(f"you are {age}, you are an adult")
elif age >= 18:
    print(f"you are {age}, you are an adult")
elif age <= 17:
    print(f"you are not an adult at {age}")

# checking multiple conditions
age_1 = 69

if age_1 <= 50 and age_1 >= 18:
    # (if age_1 <= 50) and (age_1 >= 18): can be written as this also
    print("you are eligible for bunjee jumping")
else:
    print("You are not eligible")

# Checking Whether a Value Is in a List
# to check if a value exists in a List
# use the keyword `in`
#
shells = ["bash", "zsh", "fish", "csh", "dash"]

if "bash" in shells:
    print("bash is available in the shells")

# to check something if it is not in the list
# use `not in`` keyword
if "powershell" not in shells:
    print("powershell is not available in the shells")

#
# Boolean expressions
# A booloean value is either True or False
# just like the value of a conditional after evaluation

# a boolean variable with False
is_earth_flat = False

# You do not need to add equality or inequality
# for booleans, they either return true or False
# and if takes exactly that value
if is_earth_flat:
    print("Earth is flat")
elif not is_earth_flat:
    print("Earth is round")

# the if-elif-else chain
age = 12
if age < 4:
    print("Your admission fees in $0")
elif age < 18:
    print("your admission fees is $25")
else:
    print("Your admission fees is $40")
# admission below age 4 is free
# admission for ages between 4 and 18 is $25
# and admission for more than 18 is $40

# or you can set the price first and print
# the statement later
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    prince = 40
print(f"Your admission fees is ${price}")

# Testing Multiple Conditions
# to check all conditions
# when more than one condition might be True
requested_items = ["bat", "ball", "gloves"]

if "gloves" in requested_items:
    print("We will pack gloves")

if "bat" in requested_items:
    print("We will also pack balls!")

if "gloves" in requested_items:
    print("We will also pack gloves!")

# however if we use if-elif-else on the above scenario
# it wouldn't serve the purpose, rather than checking
# all conditions it will skip all the conditions after
# passing one of them

# Using If Statements with Lists
requested_apparel = ["shoes", "socs", "tshirts", "hoodies"]

for item in requested_apparel:
    print(f"adding {item} to your cart")

print("Your cart is ready! please checkout")

# but now there ain't any socs
for item in requested_apparel:
    if item == "socs":
        print("Sorry, we currently do not have more socs")
    else:
        print(f"Adding {item} to your cart")

print("Your cart is ready! please checkout")

# Checking That a List is not Empty
requested_apparel = []

if requested_apparel:  # this condition checks for the non-emptiness of the list
    # if the list is empty it returns False
    # if it isn't it returns True
    for item in requested_apparel:
        if item == "socs":
            print("Sorry, we currently do not have more socs")
        else:
            print(f"Adding {item} to your cart")
    print("Your cart is ready! please checkout")
else:
    print("First add items to your list sir")

# Using Multiple Lists
available_veggies = [
    "onion",
    "potato",
    "cucumber",
    "carrot",
    "raddish",
    "brinjal",
    "watermelon",
    "pumpkin",
]

requested_veggies = ["onion", "bitterguard", "broccoli", "pumpkin", "potato"]

for requested_veggie in requested_veggies:
    # here after one item is choosen by the if loop, the item is
    # further tested by an if conditional
    # to check if it is in the available_veggies list
    if requested_veggie in available_veggies:
        print(f"Adding {requested_veggie} to your cart")
    else:
        print(f"We currently do not have {requested_veggie}")

print("Your bag is ready")
