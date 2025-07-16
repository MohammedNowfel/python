# Nested Loop

n = int(input("Enter a number:"))

for j in range(1, n+1):
    for i in range(1, j+1):
        print(i, end=" ")
    print()


# Format

x = int(input("Enter a number:"))

for i in range(x):
    for j in range(x):
        print("*", end=" ")
    print()