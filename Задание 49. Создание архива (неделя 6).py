S, N = map(int, input().split())
a = list(range(N))
for i in range(N):
    a[i] = int(input())
a.sort()
k = 0
for i in range(N):
    if S >= a[i]:
        S -= a[i]
        k += 1
print(k)

# Напишите программу, которая по заданной информации о пользователях и свободному объему
# на архивном диске определит максимальное число пользователей, чьи данные можно поместить в архив.
# Программа получает на вход в одной строке число S – размер свободного места на диске
# (натуральное, не превышает 10000), и число N – количество пользователей
# (натуральное, не превышает 100), после этого идет N чисел - объем данных каждого пользователя
# (натуральное, не превышает 1000), записанных каждое в отдельной строке.
