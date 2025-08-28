bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# adding one bicycle to the end
bicycles.append("stallion")

print(bicycles)

# removing one bicycle entirely without storing it
# by index number
#
del bicycles[0]
print(bicycles)

# inserting an item to index 0
#
bicycles.insert(0, "hercules")
print(bicycles)

# removing an item and storing it
# to a variable
#
rmed_cycle = bicycles.pop()
print(rmed_cycle.title(), "is now not among us")
print(bicycles)

#
# pop() method also supports particular indexes
zeroth_cycle = bicycles.pop(0)
print(zeroth_cycle.title(), "has been removed impetuously")
print(bicycles)

#
# removing an item by value
print("redline has been causing us loss, time to remove it")
bicycles.remove("redline")
print("Our current stock consists of only", bicycles)

#
# remove an item by value
# but also use it
print("Let us remove specialized, we are going bankrupt otherwise")
item_to_remove = "specialized"
bicycles.remove("specialized")
print(item_to_remove.title(), "has been removed")
print(bicycles)

## new stonks came

# sorted() function
## print them sorted without modifying the list

bicycles = [
    "trek",
    "cannondale",
    "redline",
    "specialized",
    "hercules",
    "bsa",
    "jaguar",
    "stalion",
]
print("Now, we have new stocks, fresh from the factory!!")
print(sorted(bicycles))
print(bicycles)

# .sort() method
# sort permanently
bicycles.sort()
print(bicycles)

# .reverse() method
# make them reversed permanently
bicycles.reverse()
print(bicycles)

# len() function
# find out how many brands u have
print(len(bicycles))
