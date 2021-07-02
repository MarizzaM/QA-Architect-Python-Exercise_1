formula = input("Enter calculation of the numerical digits, format: X + Y = Z ")

lst = formula.split(" + ")
x = int(lst[0])
del lst[0]
lst = str(lst[0]).split(" = ")
y = int(lst[0])
z = int(lst[1])

if x + y == z:
    print(True)
else:
    print(False)
