
arr = [1,2,3,4,5,6]
odd = []

for i in arr:
    if(i%2==1):
        odd.append(i)
    
print(odd)

# List Comprehension

odd1 =[i for i in arr if i%2==1]
print(odd1)

even1 = [ i for i in arr if i%2==0]
print(even1)