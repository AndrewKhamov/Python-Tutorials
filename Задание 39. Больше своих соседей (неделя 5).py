def BigNeighbour(A):
    count = 0
    b = []
    for i in range(1, len(A) - 1):
        if a[i - 1] <= a[i] and a[i + 1] <= a[i]:
            count += 1
            b.append(a[i])
    return count, ' '.join(map(str, b))


a = list(map(int, input().split()))
print('\n'.join(map(str, BigNeighbour(a))))

# Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше двух своих соседей и выведите количество таких элементов
# от себя (выведи еще и сами эти элементы). Результат программы:
# Ввод: 1 3 2 5 4
# Вывод:
# 2
# 3 5
