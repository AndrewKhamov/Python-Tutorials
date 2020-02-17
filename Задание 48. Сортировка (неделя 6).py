n = int(input())
a = list(map(int, input().split()))
if len(a) == n:
    print(sorted(a))
else:
    print('error')

# Отсортируйте данный массив, используя встроенную сортировку.
