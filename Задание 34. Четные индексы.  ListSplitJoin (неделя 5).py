a = list(map(int, input().split()))
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i], end=' ')

# Отличия этой задачи от 37 - здесь мы не используем второй список, а пользуемся хитростью
# в команде print (end = ' ').