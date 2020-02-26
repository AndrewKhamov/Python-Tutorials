inFile = open('input 67.txt')
myDict = {}
line = inFile.read()
line = line.split()
print(line)
for word in line:
    if word not in myDict:
        myDict[word] = myDict.get(word, 0)
    myDict[word] += 1
keysList = list(myDict.keys())
valuesList = list(myDict.values())
print(keysList)
print(valuesList)
myList = []
for i in range(len(myDict)):
    myList.append((valuesList[i], keysList[i]))
myList.sort(key=lambda myList: myList[1])
myList.sort(key=lambda myList: myList[0], reverse=True)
print(myList)

# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их количества появления в тексте,
# а при одинаковой частоте появления — в лексикографическом порядке.
# Вывод программы:
# damme
# is
# name
# van
# bond
# claude
# hi
# my
# james
# jean
# what
# your
# Указание.
#
# После того, как вы создадите словарь всех слов, вам захочется отсортировать его по
# частоте встречаемости слова. Желаемого можно добиться, если создать список, элементами
# которого будут кортежи из двух элементов: частота встречаемости слова и само слово.
# Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет сортировать
# список кортежей, при этом кортежи сравниваются по первому элементу, а если они равны —то по второму.
# Это почти то, что требуется в задаче.
