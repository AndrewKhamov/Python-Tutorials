def get_key(myDict, value):
    for k, v in myDict.items():
        if v == value:
            return k


myDict = {}
n = int(input())
for i in range(n):
    line = input().split()
    myDict[line[0]] = line[1]
line = input()
if line in myDict:
    print(myDict[line])
else:
    print(get_key(myDict, line))

# Вам дан словарь, состоящий из пар слов. Каждое слово является
# синонимом к парному ему слову. Все слова в словаре различны.
# Для одного данного слова определите его синоним.
# Программа получает на вход количество пар синонимов N.
# Далее следует N строк, каждая строка содержит ровно два
# слова-синонима. После этого следует одно слово. Выведи синоним
