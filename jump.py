for i in range(1,11):
    if(i==5):
        continue  # jump statement
    print(i)

for i in range(1,11):
    if(i==5):
        break # it also jump statement but this is jump outside the loop
    print(i)

print("outside loop")

while(True):  # it is infinite loop and   cntl + c is used to stop the infinite loop
    print("inside loop")
    break


print("outside loop")


# Else clause in loops

for i in range(1,10):
    if i == 5:
        continue # we use break. the else part was skip
    print(i)
    
else:
    print('successfully completed!')