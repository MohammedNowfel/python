# Class

class car:
    no_of_wheels = 0
    no_of_airbags = 0
    mileage = 0.0

    def move(self):
        print("car is moving forward!")

    def reverse(self):
        print("car is moving backward!")

car1 = car()  # instance of a class - object # instantiation

car1.no_of_wheels = 4
car1.no_of_airbags = 5
car1.mileage = 20.5

print(car1.no_of_wheels)
print(car1.no_of_airbags)
print(car1.mileage)

car1.move()

car2 = car()

print(car2.mileage)

car2.no_of_wheels = 6
car2.no_of_airbags = 8
car2.mileage = 15.5

print(car2.no_of_wheels)
print(car2.no_of_airbags)
print(car2.mileage)

car2.reverse()

print(car1.mileage)



# Quiz

class Bank_Account:
    customer_name = ""
    balance = 0.0
    account_number = 0

customer1 = Bank_Account()

customer1.customer_name = str(input("Enter customer name: "))
customer1.balance = float(input("Enter balance: "))
customer1.account_number = int(input("Enter account number: "))

print(customer1.customer_name)
print(customer1.balance)
print(customer1.account_number)
