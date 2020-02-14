a = int(input('Vvedite chislo: '))
count = 1
countMax = 0
while a!= 0:
    b = a
    a = int(input('Vvedite chislo: '))
    if a == b:
        count += 1
        if count > countMax:
            countMax = count
    else:
        count = 1
print(countMax)
