# if statements return True or False
# depending on the condition

magicians = ["Alice", "David", "Dynamo", "Bayaz", "Yulwei"]

for magician in magicians:  # <---do not forget the colon here!!
    print(f"{magician.title()}, that was a great trick!")
    print(f"I cannot wait to see your next trick, {magician.title()}. \n")

    print("Thank you everyone, that was a great magic show!. \n")

# working on numerical lists
# python when used in range, starts at the first value
# and ends at the second value
# thus it doesn't print the second value
for value in range(1, 5):
    print(value)

# using range() function to make a numerical value list
# for this you have to wrap range() inside list()
# this directly converts outputs of range() to a list
# and assigns them to the provided variable
numerical_list = list(range(1, 10))
print(numerical_list)

# make a list of even numbers b/w 1 and 10
even_numbers = list(range(2, 10, 2))
print(f"even_numbers: {even_numbers}")

# make a list of odd numbers b/w 1 and 10
odd_numbers = list(range(1, 10, 2))
print(f"odd_numbers: {odd_numbers}")

# square numbers
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(f"squares of the numbers in range(1, 11) is: {squares}")

# using min() and max() functions
# to find out the maximum or minimum
# value inside a numberical list
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print("given digits are: ", digits)
print("maximum value among them is: ", max(digits))
print("minimum value among them is: ", min(digits))

# list comprehensions
# an almost magical one-liner way to generate the squared list of numbers
# or similar operations with one line only
squares = [value**2 for value in range(1, 11)]
print(squares)
