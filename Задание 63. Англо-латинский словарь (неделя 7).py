inFile = open('input 63.txt')
myDict = {}
n = int(inFile.readline())
for i in range(n):
    line = inFile.readline()
    eng = line[:line.find('-')].strip()
    latinStr = line[line.find('-') + 1:].strip()
    latins = list(map(lambda x: x.strip(), latinStr.split(',')))
    for latin in latins:
        if latin not in myDict:
            myDict[latin] = []
        myDict[latin].append(eng)
print(len(myDict))
for latin in sorted(myDict):
    print(latin, '-', ', '.join(sorted(myDict[latin])))

# Рассмотрим такую задачу: словарь задан в виде набора строк, в каждой
# строке записано слово на английском языке, затем следует символ -,
# затем, через запятую, перечислены возможные переводы слова на латынь.
# Требуется составить латино-английский словарь и вывести его в том же
# виде. Все слова должны быть упорядочены по алфавиту. Возможные переводы
# одного слова должны быть также упорядочены по алфавиту.
