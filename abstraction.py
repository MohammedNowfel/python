# Abstraction

from abc import ABC, abstractmethod

class car(ABC):
    @abstractmethod           # Decorator
    def moveForward(self):
        pass

    @abstractmethod
    def MoveBackward(self):
        pass

    @abstractmethod
    def Fm(self):
        pass

class swift(car):
    def moveForward(self):
        print("Swift is moving forward")
    
    def MoveBackward(self):
        print("Swift is moving backward")

    def Fm(self):
        print("swift is playing fm!")

class innova(car):
    # def moveForward(self):
    #     print("Innova is moving forward")
    
    def MoveBackward(self):
        print("Innova is moving backward")

    def Fm(self):
        print("Innova is playing fm!")

swift = swift()
swift.moveForward()

innova = innova()
innova.moveForward()
