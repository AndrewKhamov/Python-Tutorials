def findnumb1(myDict):
    for k, v in myDict.items():
        if v == max_val:
            return k


inFile = open('input 68.txt', encoding='utf8')
myDict = {}
n = 0

for line in inFile:
    line = line.strip()
    if line not in myDict:
        if len(myDict)<=20:
            myDict[line] = myDict.get(line, 0)
        else: break
    myDict[line] += 1
    n += 1
print(myDict)
max_val = max(myDict.values())
if max_val / n * 100 > 50:
    numb1 = findnumb1(myDict)
    print(numb1, max_val / n * 100)
else:
    numb1 = findnumb1(myDict)
    print(numb1, max_val / n * 100)
    del myDict[numb1]
    max_val = max(myDict.values())
    numb2 = findnumb1(myDict)
    print(numb2, max_val / n * 100)


# Каждая строка входного файла содержит имя кандидата, за которого отдал голос один избиратель.
# Известно, что общее число кандидатов не превосходит 20, но список кандидатов явно не задан.
# Читайте данные из файла input.txt
# Если есть кандидат, набравший более 50% голосов, программа должна вывести его имя.
# Если такого кандидата нет, программа должна вывести имя кандидата, занявшего первое место,
# затем имя кандидата, занявшего второе место. 
