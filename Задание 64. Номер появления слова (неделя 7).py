import re

myDict = {}
inFile = open('input 64.txt')
for line in inFile:
    line = re.split("[., \-!?:;\n\t]+", line.strip())
    if '' in line:
        line.remove('')
    for word in line:
        myDict[word] = myDict.get(word, 0)
        print(myDict[word], end=' ')
        myDict[word] += 1

# Во входном файле записан текст.
# Для каждого слова из этого текста подсчитайте, сколько раз
# оно встречалось в этом тексте ранее.
