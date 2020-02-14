def SumOfSquares(a):
    sum = 0
    for i in range(1,a+1):
        sum +=i**2
    return(sum)


a = int(input())
print(SumOfSquares(a))


# По данному натуральном n вычислите сумму 1²+2²+3²+...+n².
# Формат ввода
# Вводится натуральное число.