a = int(input('Vvedite chislo: '))
if a > 1:
    i = a
    while i > 1:
        if a % i == 0:
            z = i
        i-=1
    print(z)
else:
    print('Error! Chislo dolzhno bit bolshe 1')