# constructor
# Destructor
# __str__ method

class car:

    def __init__(self, carname, no_of_wheels, no_of_airbags, mileage):
        self.no_of_wheels = no_of_wheels
        self.no_of_airbags = no_of_airbags
        self.mileage = mileage
        self.carname = carname

    def __del__(self):
        print("This is destructor!", self)

    def __str__(self):
        return (self.carname)
    
    def speed(self, speed):
        print("car is moving with a speed of", speed)

car1 = car("Tata", 4, 5, 15.5)


print(car1.no_of_wheels)
print(car1.no_of_airbags)
print(car1.mileage)


car1.speed(100)

car2 = car("Inova", 6, 8, 25.5)


print(car2.no_of_wheels)
print(car2.no_of_airbags)
print(car2.mileage)


car2.speed(140)



# Quiz

class Bank_Account:

    def __init__(self, customer_name, balance, account_number):

        self.customer_name = str(customer_name)
        self.balance = float(balance)
        self.account_number = int(account_number)

    def __str__(self):
        return (self.customer_name)


customer1 = Bank_Account("J Mohammed Nowfel Badhusha", 2000, 123445677890)

print(customer1.customer_name)
print(customer1.balance)
print(customer1.account_number)
print(customer1)