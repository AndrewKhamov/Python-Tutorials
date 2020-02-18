class Student():
    name = ''
    surname = ''
    Class = 0
    score = 0


inFile = open('input 53.txt', 'r', encoding='utf8')
outFile = open('output 53.txt', 'w', encoding='utf8')
students=[]
for line in inFile:
    stats = line.split()
    student = Student()
    student.surname = str(stats[0])
    student.name = str(stats[1])
    student.Class = int(stats[2])
    student.score = int(stats[3])
    students.append(student)
# print(students[1].name)
sum9 = 0
sum10 = 0
sum11 = 0
amount9 = 0
amount10 = 0
amount11 = 0
for i in range(len(students)):
    if students[i].Class == 9:
        sum9+=students[i].score
        amount9 +=1
    if students[i].Class == 10:
        sum10+=students[i].score
        amount10 += 1
    if students[i].Class == 11:
        sum11+=students[i].score
        amount11 += 1
avg9 = sum9/amount9
avg10 = sum10/amount10
avg11 = sum11/amount11
print(avg9, avg10, avg11)
inFile.close()
outFile.close()


# Определите и выведите средние баллы участников олимпиады в 9 классе,
# в 10 классе, в 11 классе.
# Информация о результатах олимпиады записана в файле,
# каждая строка которого имеет вид:
# фамилия имя класс балл.
