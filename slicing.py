# Slicing

string = "Hello, World!"
print(string[0:5:1]) # [start:end:step]

fruits = ("apple", "banana", "cherry", "date", "elderberry")
print(fruits[4:0:-1])# Reverse slicing

flowers = ["rose", "tulip", "daisy", "sunflower", "lily"]
print(flowers[2:5])


#quiz

numbers = [2,5,1,8,4]
print(numbers[1:4])

numbers[2:4] = [3,7]
print(numbers) 