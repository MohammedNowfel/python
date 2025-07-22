# Tuples

tup =(1,2,3,4,5)

print(tup)
print(type(tup))
print(tup[1])  # Accessing an element

# tup[0]= 1000  # This will raise an error because tuples are immutable

# Tuple methods

# Length of the tuple
print(len(tup))

# Min and Max elements in the tuple
print(min(tup))
print(max(tup))

# Count of an element in the tuple
print(tup.count(2))

# Index of an element in the tuple
print(tup.index(3))

# Tuple to list conversion
list = list(tup)
print(list)
print(type(list))

# List to tuple conversion
tup = tuple(list)
print(tup)
print(type(tup))

# one element tuple
one_element_tuple = (1,)  # Note the comma


# quiz

fruits = ("apple", "banana", "cherry", "date")
print(fruits)

fruits += ("elderberry",)  # Concatenation
print(fruits)