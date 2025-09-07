# Inheritence

# A class can inherit properties and methods from another class.

# Single Inheritence

class vehicles:
    no_of_wheels = 4

    def move(self):
        print("vehicle is moving!")

class car(vehicles):
    no_of_airbags = 5

car1 = car()
print(car1.no_of_airbags)
print(car1.no_of_wheels)
car1.move()


# Hierarchical Inheritence

class vehicles:
    no_of_wheels = 4

    def move(self):
        print("vehicle is moving!")

class car(vehicles):
    no_of_airbags = 5

class bike(vehicles):
    mileage = 60

car1 = car()
print(car1.no_of_airbags)
print(car1.no_of_wheels)
car1.move()

bike1 = bike()
print(bike1.mileage)
print(bike1.no_of_wheels)
bike1.move()

# Multi-level Inheritence

class vehicles:
    no_of_wheels = 4

    def move(self):
        print("vehicle is moving!")

class car(vehicles):
    no_of_airbags = 5

class Tata(car):
    mileage = 30

Tata = Tata()
print(Tata.no_of_wheels)
print(Tata.no_of_airbags)
print(Tata.mileage)
Tata.move()

# Multiple Inheritence

class father:
    eye_color = "blue"
    hair_color = "white"

class mother:
    hair_color = "black"

class child(mother, father): # This is called diamond problem, this gives first priority for first parent in the class. So, mother class is given priority
    no_of_legs = 2

child = child()
print(child.eye_color)
print(child.hair_color)
print(child.no_of_legs)

# Quiz

class father:
    eye_color = "blue"
    hair_color = "white"

    def music(self):
        print("Kuthu songs....!")

class mother:
    hair_color = "black"

    def music(self):
        print("melody songs....!")

class child(mother, father): # This is called diamond problem, this gives first priority for first parent in the class. So, mother class is given priority
    no_of_legs = 2

child = child()
print(child.eye_color)
print(child.hair_color)
print(child.no_of_legs)
child.music()