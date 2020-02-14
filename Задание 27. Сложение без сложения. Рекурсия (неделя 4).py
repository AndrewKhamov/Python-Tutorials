# ЧУТЬ НЕ ПОГИБ, НО ДЕЛО СДЕЛАНО


def sum(a, b):
    if a == 0 and b == 0:
        return 0
    if a > 0:
        return sum(a - 1, b) + 1
    if b > 0:
        return sum(a, b - 1) + 1

    # if a > 0 and b > 0:
    #     if a > b:
    #         return sum(a-1,b)+1
    #     if b > a:
    #         return sum(a, b-1) + 1
    #     return sum(a-1,b-1)+2


a = int(input())
b = int(input())
print(sum(a, b))

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
