n = int(input('Vvedite chislo: '))
i=1
while i**2 <= n:
    print(i**2, end = " ")
    i+=1
print('\nVsego kvadratov: ', i-1)
