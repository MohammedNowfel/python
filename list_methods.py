# List methods in Python

lst_1 = [1,2,3,4,5]
lst_2 = [7,8,9]

# Length of the list
print(len(lst_1))

# Inserting one element into the list
lst_1.append(6)
print(lst_1)

# Inserting set of elements into the list
lst_1.extend(lst_2)
print(lst_1)

# Inserting an element at a specific index
lst_1.insert(0,0)
print(lst_1)

# Counting the elements in the list
print(lst_1.count(1))

# Finding the index of an element in the list  # Index finds the first occurrence
print(lst_1.index(5))

# Min and Max elements in the list
print(min(lst_1))
print(max(lst_1))



lst_2.extend(lst_1)
print("Before sorting:", lst_2)

# Sorting the list

# Ascending order
lst_2.sort()
print("After sorting in ascending order:", lst_2)

# Descending order
lst_2.sort(reverse=True)
print("After sorting in descending order:", lst_2)


# Sum of elements in the list
print(sum(lst_2))

# Mutablity
lst_1[0]= 1000
print(lst_1)

# Remove 
lst_1.remove(1000) # it removes the first occurrence of the value 1000 from the list
print(lst_1) 

# Pop
lst_1.pop(0)  # if don't give index, removes the last element
print(lst_1)


# Clearing the list
lst_2.clear()
print(lst_2)




