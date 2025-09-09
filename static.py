

class swift():
    @staticmethod
    def moveForward():
        print("Swift is moving forward")
    
    def MoveBackward():  # dont use self here
        print("Swift is moving backward")

    def Fm(self):
        print("swift is playing fm!")

swift.moveForward()   # This is how we call static method without creating an object of the class

swift.MoveBackward()


# class variable and instance variable

class Father:
    age = 0       #class variable
    def __init__(self):
        self.name = "Father"          #instance variable
        print("Father constructor")

    def say_hello(self):
        print("Hello from Father!")

father1 = Father()
father2 = Father()

print(father1.age)  # accessing class variable using object
father1.age = 50 
print(father1.age) # it will create a new instance variable for father1 object
Father.age = 40  # modifying class variable using class name
print(father2.age) # it will access class variable