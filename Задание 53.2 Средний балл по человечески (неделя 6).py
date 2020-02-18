def sum(A):
    sum = 0
    for i in range(len(A)):
        sum += A[i]
    return sum


inFile = open('input 53.txt', 'r', encoding='utf8')
class9 = []
class10 = []
class11 = []
for line in inFile:
    a = line.split()
    if '9' in a[2]:
        class9.append(int(a[3]))
    elif '10' in a[2]:
        class10.append(int(a[3]))
    elif '11' in a[2]:
        class11.append(int(a[3]))
avg9 = sum(class9) / len(class9)
avg10 = sum(class10) / len(class10)
avg11 = sum(class11) / len(class11)
print(avg9, avg10, avg11)
inFile.close()
# Определите и выведите средние баллы участников олимпиады в 9 классе, в 10 классе, в 11 классе.
# Информация о результатах олимпиады записана в файле, каждая строка которого имеет вид:
#
# фамилия имя класс балл.
# Выведите три числа: средние баллы по 9 классу, по 10 классу, по 11 классу.
