#Ублюдский код, но хоть работает...
def ReduceFraction(a,b):
    amin = 1
    bmin = 1
    for i in range(1, max(a,b)):
         if a % i == 0 and b % i == 0:
            imin = i
            if a//imin < a//amin and b//imin < b//bmin:
                amin=imin
                bmin =imin
    return a//amin, b//bmin


a = int(input())
b = int(input())
print(*ReduceFraction(a,b))


# Даны два натуральных числа n и m.
# Сократите дробь (n / m), то есть выведите два других числа p и q таких,
# что (n / m) = (p / q) и дробь (p / q) — несократимая.
# Решение оформите в виде функции ReduceFraction(n, m),
# получающая значения n и m и возвращающей кортеж из двух чисел: return p, q.
# Тогда вывод можно будет оформить как print(*ReduceFraction(n, m)).
