# Scope of variables

def add():
    global a  # to use the global variable inside the function
    a = a+5  
    b = 10 # local variable
    print(a+b)


a = 15 # global variable
b = 20 # global variable

add()
print(a+b)

#quiz

x = 10
def change_X():
    x = 20   # if you want to change the globel value you use (global x) keyword

change_X()

print(x)