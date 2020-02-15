a = list(map(int, input().split()))
b = []
for i in range(1,len(a)):
    if a[i] > a[i-1]:
        b.append(a[i])
print(' '.join(map(str, b)))

#Отличия этой задачи от 34,35 - здесь мы используем второй список и выводим его через join.