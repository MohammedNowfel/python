# Polymorphism

# Compile-time polymorphism (Method Overloading)

'''
In other programming languages

int sum(int a, int b){
    return a + b;
    }

float sum(float a, float b){
    return a + b;
    }

int sum(int a, int b, int c){
    return a + b + c;
    }

sum(10, 20);        // 30
sum(10.5, 20.5);    // 31.0
sum(10, 20, 30);    // 60

'''

# In python

class summation:

    def sum(self, *args):
        ans = 0
        for i in args:
            ans +=i
        return ans
    
sum1 = summation()
print(sum1.sum(10,20,30,40,50))

# Run-time polymorphism (Method Overriding)

class Father:
    def __init__(self):
        print("Father constructor")

    def say_hello(self):
        print("Hello from Father!")

class Son(Father):
    def __init__(self):
        print("Child constructor")

    def say_hello(self, name):
        print("Hello from Son!", name)

son = Son()
son.say_hello("Nowfel")

father = Father()
father.say_hello()