class Matrix:
    def __init__(self, list):
        self.lines = []
        self.n = len(list)
        self.k = len(list[1])
        for i in range(len(list)):
            self.lines.append(list[i])

    def __str__(self):
        newlines = ''
        for i in range(len(self.lines)):
            # newlines = ''
            for j in range(len(self.lines[i])):
                newlines += str(self.lines[i][j]) + '\t'
            newlines = newlines.rstrip()
            newlines += '\n'
        self.newlines = newlines.rstrip()
        return self.newlines

    def size(self):
        return (self.n, self.k)

    def __mul__(self, other):
        makestr = str(self)
        multlines = ''
        for el in makestr:
            if el == '\t':
                multlines += '\t'
            elif el == '\n':
                multlines += '\n'
            else:
                multlines += str(int(el) * other)
        return multlines

    __rmul__ = __mul__

    def __add__(self, other):
        result = []
        resultTup = []
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                resultTup.append(self.lines[i][j] + other.lines[i][j])
            result.append(resultTup)
            resultTup = []
        return str(Matrix(result))


a = Matrix([[1, 0, 0], [1, 1, 1], [0, 0, 0]])
b = Matrix([[10, 5, 1], [0, 4, 1], [100, 60, 90]])
print(a + b)
print('\n')
print(a.size())
print('\n')
print(b * 10)
print('\n')
print(Matrix([[0, 1], [1, 0]]) * 10)

# Добавьте в предыдущий класс следующие методы:
#
# __add__, принимающий вторую матрицу того же размера и возвращающий сумму матриц.
# __mul__, принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр.
# __rmul__, делающий то же самое, что и __mul__. Этот метод будет вызван в том случае, аргумент
# находится справа. Для реализации этого метода в коде класса достаточно написать __rmul__ = __mul_
