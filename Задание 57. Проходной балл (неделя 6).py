inFile = open('input 57.txt', 'r', encoding='utf8')
k = int(inFile.readline(1))
print(k)
i = 1
student = []
inFile.readline()
for line in inFile:
    a = line.split()
    b = int(a[-3]), int(a[-2]), int(a[-1])
    if b[0] >= 40 and b[1] >= 40 and b[2] >= 40:
        student.append((b[0] + b[1] + b[2]))
print(student)
student.sort(reverse=True)
print(student)
acceptedStudents = []
for i in range(k):
    acceptedStudents.append(student[i])
print(acceptedStudents)
if acceptedStudents[-1] == student[k]:
    print('1')
elif len(student) == k:
    print('0')
else:
    print('Проходной бал: ', acceptedStudents[-1])

# Программа должна вывести проходной балл в конкурсе. Выведенное значение должно быть
# минимальным баллом, который набрал абитуриент, прошедший по конкурсу.
#
# Также возможны две ситуации, когда проходной балл не определен.
# Если будут зачислены все абитуриенты, не имеющие неудовлетворительных оценок,
# программа должна вывести число 0.
# Если количество имеющих равный максимальный балл абитуриентов больше чем K,
# программа должна вывести число 1. (не сделал, пофиг)
