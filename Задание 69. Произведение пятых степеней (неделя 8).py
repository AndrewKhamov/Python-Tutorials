from functools import reduce


def prod(a, b):
    return a * (b ** 5)


myList = list(map(int, input().split()))
myList[0] **= 5
print(myList)
print(reduce(prod, myList))

# На вход подаётся последовательность натуральных чисел длины n≤1000.
# Посчитайте произведение пятых степеней чисел в последовательности.
# Для решения задачи используйте функцию reduce из модуля functools
