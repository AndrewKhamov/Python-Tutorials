def CountSort(A):
    b = []
    length = len(A)
    for i in range(length):
        b.append(min(A))
        A.remove(min(A))
    return b


a = list(map(int, input().split()))
print(' '.join(map(str, CountSort(a))))

# Отсортируйте список в порядке неубывания элементов. Выведите полученный список.
#  Решение оформите в виде функции CountSort(A), которая модифицирует передаваемый ей список.
#  Использовать встроенные функции сортировки нельзя.
