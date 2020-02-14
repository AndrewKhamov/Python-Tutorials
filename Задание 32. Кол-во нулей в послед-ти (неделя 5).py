def ZeroCounter(n):
    count = 0
    for i in range(n):
        a = int(input())
        if a == 0:
            count+=1
    return count


n = int(input())
print(ZeroCounter(n))


# Дано несколько чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.
# Формат ввода
# Cначала вводится число N, затем вводится ровно N целых чисел.