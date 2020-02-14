a = int(input('Skolko rublei stoit pirozhok: '))
b = int(input('Skolko kopeek stoit pirozhok: '))
n = int(input('Skolko pirozhkov: '))
b = b*n
a = a*n
print(a + b//100, ' rublei i ', b % 100, ' kopeek')