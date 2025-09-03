# Recursive Function

def add(n):

    print(n)

    if (n==100):       # Base case
        return 100

    return add(n+1)    # Recursive case

add(0)


# factorial

def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n-1)

print(factorial(5))