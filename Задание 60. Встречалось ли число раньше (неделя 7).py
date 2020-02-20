myList = list(map(int, input().split()))
mySet = set()
for digit in myList:
    if digit not in mySet:
        print('NO')
        mySet.add(digit)
    else:
        print('YES')

# Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось
# в последовательности или NO, если не встречалось.
# Вводится список чисел. Все числа списка находятся на одной строке.
