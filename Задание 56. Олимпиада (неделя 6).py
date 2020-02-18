n = int(input())
listOf = []
for i in range(n):
    a = input().split()
    listOf.append((a[0], int(a[1])))
listOf.sort(key=lambda listOf: -listOf[1])
for i in range(len(listOf)):
    print(listOf[i][0])

# Программа получает на вход число участников олимпиады N. Далее идет N строк,
# в каждой строке записана фамилия участника, затем, через пробел, набранное им количество баллов.
# Выведите список участников (только фамилии) в порядке убывания набранных баллов.
