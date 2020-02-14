a = int(input('vvedite chislo: '))
if -1000 <= a <= 1000:
    print('The next number for the number ', a, ' is ', a+1)
    print('The previous number for the number ', a, ' is ', a-1)
else:
    print('Error')
