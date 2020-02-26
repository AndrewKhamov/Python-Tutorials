def max(myDict):
    kmax = 0
    vmax = 0
    for k, v in myDict.items():
        if v > vmax:
            vmax = v
            kmax = k
        if v == vmax:
            if k < kmax:
                kmax = k
    return kmax


text = input().split()
myDict = {}
for word in text:
    if word not in myDict:
        myDict[word] = myDict.get(word, 0)
    myDict[word] += 1
print(myDict)
print(max(myDict))

# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# Входные данные:
# apple orange banana banana orange
#
# Вывод программы:
# banana
