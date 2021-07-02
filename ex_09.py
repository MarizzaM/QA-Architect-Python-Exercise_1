n1 = int(input('PLease enter number 1: '))
n2 = int(input('PLease enter number 2: '))
n3 = int(input('PLease enter number 3: '))

if n1 != n2 and n1 != n3 and n2 != n3:
    if n1 > n2 and n1 > n3:
        print(f'number {n1} is the biggest')
    elif n2 > n3:
        print(f'number {n2} is the biggest')
    else:
        print(f'number {n3} is the biggest')
else:
    print('Similar numbers')
