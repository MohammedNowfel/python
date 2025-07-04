# Nested If

age = 18
eat_pizza = False
exercise = False

if(age<30):
    if(eat_pizza):
        print('Unfit')
    else:
        print('Fit')

else:
    if(exercise):
        print('Fit')
    else:
        print('Unfit')


# Ternary Operator

print('child' if (age<18) else 'Adult')


# Ternary Operator with multiple conditions

print("unfit" if (eat_pizza) else "fit" if (age<30) else "fit" if (exercise) else "unfit")