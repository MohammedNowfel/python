age = 30
income = 20000

if(age < 18):
    message = "you are too young to work"

elif(age >=18 and age <=25):
    if(income <= 30000):
        message = "you are eligible for a student offer"
    else:
        message = "you are eligible for only a regular offer"

else:
    message = "you are eligible for only a regular offer"

print(message)