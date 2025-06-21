#!/usr/bin/env python3

# the range() function starts counting from '1' and ends with '6'
# and because it stops at the second values, the output never contains that value
# this is called off-by-one behaviour in programming languages
#
for value in range(1,6):
    print(value)

# using range() to make a list of numbers
numbers = list(range(1,6))
print(numbers)

# skip some numbers
# A third argument in range() is considered as a step size
# when generating numbers
# the range function starts from first argument
# stops at second
# adds the step of third argument
even_numbers=list(range(2,11,2))
print(even_numbers)

odd_numbers=list(range(1,11,2))
print(odd_numbers)

# list of square numbers of first 10 natural numbers
squares = []
for value in range(1,11):
    square = value ** 2 # temporary variable
    squares.append(square)
print(squares)

# method2
squares = [ ]
for value in range(1,11):
    squares.append(value**2)
print(squares)
