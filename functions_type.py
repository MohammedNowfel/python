# # Void Functions
# # doesn't return a value is called void function

# def add():
#     a = int(input())
#     b = int(input())
#     print(a+b)

# sum1 = add()
# print(sum1)  # None



# # non-void Functions
# # returns a value is called non-void function

# def add():
#     a = int(input())
#     b = int(input())
#     return a+b

# sum1 = add()
# print(sum1)  # 10



# Example

def sum(a,b):
    return a+b

def sub(a,b):
    return a-b 

def mul(a,b):
    return a*b

a = int(input())
b = int(input())

sum_1 = sum(a,b)
sub_1 = sub(a,b)
mul_1 = mul(a,b)

print("Sum:", sum_1)
print("Subtraction:", sub_1)
print("Multiplication:", mul_1)

#quiz

def area_of_rectangle(length, width): # Parameters
    return length * width

rectangle_area = area_of_rectangle(5,3) # Positional Arguments
print(rectangle_area)


# Types of Arguments

    #keyword arguments - area_of_rectangle(length=5, width=3)
    #default arguments - def area_of_rectangle(length, width=3):  (used in last)
    #positional arguments - area_of_rectangle(5, 3)   (used in first)



#quiz

def greet(name, message = "Hello"):
    print(message, name + "!")

greet("Nowfel")
