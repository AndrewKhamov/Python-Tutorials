def factorial(a):
    if a > 1:
        return a*factorial(a-1)
    return 1

n = int(input())
sum=0
for i in range(1,n+1):
    sum+=factorial(i)
print(sum)


# По данному натуральному n вычислите сумму 1!+2!+3!+...+n!.
# В решении этой задачи можно использовать только один цикл.
# Формат ввода
# Вводится натуральное число n.