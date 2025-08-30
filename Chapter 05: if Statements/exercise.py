# 5-1. Conditional Tests
# Write a series of conditional tests
# Print statements describing each test
car = "tata"

print("is car == 'subaru'? I predict false")
print(car == "subaru")

print("is car == 'tata'? I predict true")
print(car == "tata")

planet = "Earth"

print("is planet == 'earth' I predict true")
print(planet.lower() == "earth")

print("is planet == 'mars' I predict false")
print(planet.lower() == "mars")

# I conclude that, if runs solely on True and False
# results from the conditionals like equality, inequality,
# but for booleans they are objects with either True
# or False value and they represent their values
# hence when you use if <a boolean variable>, it operates
# on the fact is the boolean is True or False
#

# 5-2.1: Test for equality and inequality

age = 17
if age <= 18:
    print("You are not an adult")

age = 19
if age >= 18:
    print("You are an adult")

# 5-2.2: Test using the lower() method

car = "HoolaHayaBusaMercedes"

if car.lower() == "hoolahayabusamercedes":
    print("yes car is, HoolaHayaBusaMercedes")

# check using and and or
age = 18
if age > 17 or age == 18:
    print("you are an adult at: ", age)

number_1 = 10
number_2 = 12
if number_1 == number_2:
    print("both numbers are same")
elif number_1 < number_2:
    print(f"{number_1} is smaller than {number_2}")
elif number_2 > number_1:
    print(f"{number_2} is smaller than {number_1}")

number = 30
if number > 29 and number < 31:
    print("you number is 30")

# 5-2.3: check if an item is in a list
vegetables = ["onion", "gian", "carrot", "ladyfinger", "broccoli"]
if "onion" in vegetables:
    print("onions are in stock")

# 5-2.4: check if an item is not in a list
if "tomato" not in vegetables:
    print("Tomatoes are not in stock")

# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game,
# create a variable called alien_color and assign it a value of 'green',
# 'yellow' or 'red'
# write if statement to check if it is green, and print a message that
# the player earned 5 points
alien_color = "red"
if alien_color == "green":
    print("You earned 5 points")
elif alien_color == "red":
    print("You are a red, darling!")

# the same program without output
if alien_color == "green":
    print("You earned 5 points")

# 5-4. Alien Colors #2: Choose a color for an alien, write if-else chain
# if color's green print player earned 5 pts by shooting the alien
# if color's not green he earned 10pts
# write one version running if and one running else
alien_color = "yellow"

if alien_color == "green":
    print("You have just earned 5 pts by shooting a green alien")
else:
    print("You have just earned 10 pts by shooting a non-green alien")

# or
if not alien_color == "green":
    print("You have just earned 10 pts by shooting a non-green alien")

# or
if alien_color != "green":
    print("You have just earned 10 pts by shooting a non-green alien")

# 5-5. Alien Colors #3: turn 5-4 to if-elif-else
# v1
if alien_color == "green":
    print("You got 5 pts")
elif alien_color == "red":
    print("you got 15 pts")
else:
    print("you got 10 points")
# v2
if alien_color == "red":
    print("You got 15 pts")
elif alien_color == "yellow":
    print("you got 10 pts")
else:
    print("you got 5 points")
# v3

if alien_color == "yellow":
    print("You got 10 pts")
elif alien_color == "red":
    print("you got 15 pts")
else:
    print("you got 5 points")

# 5-6. Stages of Life
# write if-elif-else block to determine
# a person's stage of life
age = 33
if age < 2:
    person = "baby"
elif age < 4:
    person = "toddler"
elif age < 14:
    person = "kid"
elif age < 20:
    person = "teenager"
elif age < 65:
    person = "adult"
elif age >= 65:
    person = "elder"
else:
    person = "dead"

print(f"the person is {person}")

# 5-7. Favourite fruit: Make a list of favourite fruits of three
# write 5 if statements each should check whether a certain kind of fruit is
# in your list
favourite_fruits = ["apple", "banana", "grapes"]

if "grapes" in favourite_fruits:
    print("you like grapes")

if "banana" in favourite_fruits:
    print("you like banana")

if "orange" in favourite_fruits:
    print("you like orange")

if "guava" in favourite_fruits:
    print("you like guava")

if "jackfruit" in favourite_fruits:
    print("you like jackfruit")

# 5-8. Hello Admin: Make a list of 5+ usernames, including the name
# 'admin', it greeets each user after they log in
# loop through the list and greet each of them
# if user is admin, print a special greeting
# otherwise it must be generic

users = ["bob", "kant", "shakespeare", "nietzsche", "newton", "admin"]

for user in users:
    if user == "admin":
        print("Hello dear administrator. \nWould you like to see the cache hits?")
    else:
        print(f"Hello {user}, thank you for loggin in")

# 5-9. No Users: add an if test to hello_admin.py to make sure
# users are not empty

users_2 = []

if users_2:
    for user in users_2:
        if user == "admin":
            print("Hello dear administrator. \nWould you like to see the cache hits?")
        else:
            print(f"Hello {user}, thank you for loggin in")
else:
    print("no users found")

# 5-10. Checking Usernames
# check if any username is reused
current_users = ["alice", "bob", "darrow", "neuro", "octavia"]

new_users = ["roque", "adrius", "virginia", "darrow"]

for user in new_users:
    if user not in current_users:
        print(f"{user} username is available")
    else:
        print(f"{user} username is already used!! \nchoose a different one")
# make it case insensitive
new_users = ["Roque", "Adrius", "Virginia", "Darrow"]

new_users_converted = [user.lower() for user in new_users]

for user in new_users_converted:
    if user not in current_users:
        print(f"{user} username is available")
    else:
        print(f"{user} username is already used!! \nchoose a different one")

# 5-11. Ordinal Numbers
# a list of numbers from 1 to 9
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
