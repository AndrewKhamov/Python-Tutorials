a = 'gpthgpthgggggggghgggh'
pos = a.find('h')
print(pos)
if pos != -1:
    b1 = pos + 1
    while pos != -1:
        print(pos)
        pos = a.find('h', pos + 1)
    b2 = pos
    print(a[:b1 - 1], a[b1:b2], sep='')

# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h
#
