# Encapsulation

class car:

    def __init__(self, no_of_wheels, no_of_airbags, mileage):
        self.__no_of_wheels = no_of_wheels   # private variable
        self.no_of_airbags = no_of_airbags
        self.mileage = mileage

# Getter method
    def get_no_of_wheels(self):
        return ("No of wheels:", self.__no_of_wheels)
    
# Setter method
    def set_no_of_wheels(self, no_of_wheels):
        self.__no_of_wheels = no_of_wheels

car1 = car(4, 5, 15.5)

print(car1.get_no_of_wheels())
print(car1.no_of_airbags)
print(car1.mileage)


car1.__no_of_wheels = 6  # direct access to private variable is not possible # but this will create a new variable
print(car1.__no_of_wheels)  # this will print the new variable
print(car1.get_no_of_wheels())  # this will print the private variable

car1.set_no_of_wheels(8)
print(car1.get_no_of_wheels())
