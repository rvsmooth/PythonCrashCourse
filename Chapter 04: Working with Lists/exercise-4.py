# 4-1. Pizzas: Make a pizza list
pizzas = ["margherita", "diabola", "hawaiian", "marinara", "veronese", "pepperoni"]

# 4-1.1: use for loop to print a sentence using the name of the pizza
for pizza in pizzas:
    print(f"I like {pizza}. \n")
print("I really love pizzas :D")

# 4-2. Animals: Make a list of animals having common characteristic
animals = ["lion", "tiger", "hyena", "wolf", "cheetah"]

for animal in animals:
    print(animal)

# 4-2.1: Modify the program to print a statement about each animal
for animal in animals:
    comment = f"A {animal} is dangerous, beware of it."
    print(comment)

# 4-2.2: at the end of the program print a line that is common about them
print("They all are bloody carnivorous")

# 4-3. counting to twenty use a for loop to print from 1 to 20 (inclusive)
# 1. using list comprehensions
squares = [print(value) for value in range(1, 21)]

# using general method
squares = list(range(1, 21))
for value in squares:
    print(value)

# 4-4. Make list of numbers from one to one million, then use a loop to
# print the numbers
# close it if it takes too much time :)
numbers = [print(value) for value in range(1, 1000001)]
# the above method doesn't create a list actually

# 4-5. Summing a million
# Make list of numbers from one to one million and then use min() and
# max() to ensure it ends at one milion and starts from one
# use sum() to see the sum of them!!
numbers = [value for value in range(1, 1000001)]
# this above method creates a list
print(f"smallest number in range(1, 1000001) is: {min(numbers)}")
print(f"biggest number in range(1, 1000001) is: {max(numbers)}")
print(f"sum of numbers in range(1, 1000001) is: {sum(numbers)}")

# 4-6. Odd numbers: use third argument of range() to make a list of odd
# numbers from 1 to 20 and print each of them
numbers = [number for number in range(1, 20, 2)]
print(numbers)
for value in numbers:
    print(value)

# 4-7. Threes: Make a list of multiples of 3 from 3 to 30, and print each with for
numbers = [number * 3 for number in range(3, 31)]
for value in numbers:
    print(value)

# 4-8. Cubes: Make a list of the first 10 cubes print each with for
numbers = [number**3 for number in range(1, 11)]
for value in numbers:
    print(value)
