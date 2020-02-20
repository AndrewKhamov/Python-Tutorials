import re

inFile = open('input 61.txt', 'r', encoding='utf8')
wordsSet = set()
for line in inFile:
    a = re.split("[., \-!?:;\n]+", line)  # офигенная штука, единственное с чем не справляется -
    print(a)                            # - конец файла. Оставляет пустой символ. Исправляю в самом конце
    for word in a:
        if word not in wordsSet:
            wordsSet.add(word)
print(wordsSet)
print(len(wordsSet))
wordsSet.remove('')
print(len(wordsSet))

# Во входном файле записан текст. Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.
