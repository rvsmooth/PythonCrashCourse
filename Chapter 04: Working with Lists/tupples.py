# tuples are like lists but with parenthesis
# but immutable, ie., you cannot change their values
# and they remain fixed
#
#
# tuples are defined, technically, by the presence of a comma

# an example of a tuple with on element
tuple_a = (1,)
print(tuple_a[0])

# tuples can be looped over
tuple_b = (1, 2, 3, 5, 20)

for i in tuple_b:
    s = i * i
    print("the square of", i, "is", s)

# although elements of a tuple remain immutable
# the tuple itself isn't
# that is, tuple, as any variable, can be replaced

# first tuple, tuple_i
tuple_i = (50, 100)
print("Initial tuple", tuple_i)

tuple_i = (100, 50)
print("Final tuple", tuple_i)

# compared to lists, tuples are simple data structures
# use them to store a set of value that needn't changing
#
# for example you might need to, sometimes, change entire
# data sets instead of specific values, and that's when
# you utilities tuples
