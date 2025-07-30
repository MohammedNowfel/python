# Dictionary 

# This is collection of unordered pairs

num = {1:'One', 2:'Two'}  # only use the immutable datatypes for keys and use any datatype for values

print(num)
print(type(num))

print(num[2])
# print(num[7])   # It is through the key error


# methods

# accessing - num[1]
print(num.get(1))

# Length
print(len(num))

# Keys
print(num.keys())

# Values
print(num.values())

# items
print(num.items())

# insert
num[3]= 'Three'    # The key already in the dict means that is updated and not in the dict means add that
print(num)        

# remove
num.pop(3)#keys       # if you give the wrong keys that throw the keyerror
print(num)

# clear
num.clear()
print(num)

# empty dict
num = dict()
print(num)

# Quiz

map = {5: {'p':{5:"p"}, 6:"q"},
        7:"r",
          'q':"s",
            "s":'t'}

print(map[map[map[5][6]]])