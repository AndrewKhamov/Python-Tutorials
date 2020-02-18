class Man():
    surname = ''
    name = ''
    score = ''


# def manKey(man):
#     return (man.surname)


inFile = open('input 54.txt', 'r', encoding='utf8')
outFile = open('output 54.txt', 'w', encoding='utf8')
peopleList = []
for line in inFile:
    a = line.split()
    man = Man()
    man.surname = a[0]
    man.name = a[1]
    man.score = a[3]
    peopleList.append(man)
peopleList.sort(key=lambda man: man.surname)
for man in peopleList:
    print(man.surname, man.name, man.score, file=outFile)
inFile.close()
outFile.close()

# Известно, что фамилии всех участников — различны. Сохраните в массивах список всех участников
# и выведите его, отсортировав по фамилии в лексикографическом порядке.
# При выводе указываете фамилию, имя участника и его балл.
#
# Используйте для ввода и вывода файлы input.txt и output.txt с указанием кодировки utf8.
