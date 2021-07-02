formula = input("PLease enter calculation, format: X + Y = Z ")

lst = formula.split()
x = int(lst[0])
y = int(lst[2])
z = int(lst[4])

if x + y == z:
    print(True)
else:
    print(False)
