# Set 
# It is hetrogenious
# It is unordered

set1 = {1,2,3,4,5,1,2} # it is not accept duplecate values
print(set1)
print(type(set1))

set1.add("1")
print(set1)

set1.remove(1)
print(set1)

set1.clear()
print(set1)

lst= [1,2,3,4]
set2 = set(lst) #same as tuple
print(set2)



#Set Operation

set_1 = {1,2,3,4}
set_2 = {3,4,5,6}

#Union
print(set_1.union(set_2))

#Intersection
print(set_1.intersection(set_2))

#Difference
print(set_1.difference(set_2))

#Traversal
for i in set_1:
    print(i)

#Membership Operator
print('1' in set_1)



# Quiz

s1={1,2,3,4}
s2={4,5}
s3={2,3,4,5,7,8}
print(s1.union(s2).intersection(s3))