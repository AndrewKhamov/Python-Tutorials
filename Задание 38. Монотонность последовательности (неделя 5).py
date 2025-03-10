def IsAscending(A):
    i = 1
    count = 1
    while 1 <= i < len(A) and a[i] > a[i - 1]:
        count += 1
        i += 1
    return (count)


a = list(map(int, input().split()))
b = (IsAscending(a))
if b == len(a):
    print('YES')
else:
    print('NO')

# Дан список. Определите, является ли он монотонно
# возрастающим(то есть верно ли, что каждый элемент этого списка
# больше предыдущего).Выведите YES, если массив монотонно возрастает
# и NO в противном случае.Решение оформите в виде функции IsAscending(A).
# В данной функции должен быть один цикл while, не содержащий вложенных
# условий и циклов — используйте схему линейного поиска.
