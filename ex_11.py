formula = input("PLease enter calculation, format: X + Y = Z ")

lst = formula.split()
x = int(lst[0])
operator = lst[1]
y = int(lst[2])
z = int(lst[4])

if operator in ["+", "-", "/", "*"]:
    if operator == "+":
        if x + y == z:
            print(True)
        else:
            print(False)
    elif operator == "-":
        if x - y == z:
            print(True)
        else:
            print(False)
    elif operator == "*":
        if x * y == z:
            print(True)
        else:
            print(False)
    elif operator == "/":
        if y != 0:
            if x / y == z:
                print(True)
            else:
                print(False)
        else:
            print('Error: Div by zero')
else:
    print(f'{operator} is an illegal operator')
