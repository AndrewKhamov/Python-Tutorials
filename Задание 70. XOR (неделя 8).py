a = list(map(int, input().split()))
b = list(map(int, input().split()))
c1 = []
for i in range(min(len(a), len(b))):
    c1.append(a[i].__xor__(b[i]))
print(' '.join(map(str, c1)))

# Булева функция XOR (сложение по модулю два) задаётся следующей
# таблицей истинности:
# xor(0,0)=0
# xor(0,1)=1
# xor(1,0)=1
# xor(1,1)=0
# На вход подаются две последовательности (a₁,…,an) и (b₁,…,bn) из 0 и 1.
# Вычислите последовательность из (c₁,…,cn), где каждая cᵢ=xor(aᵢ,bᵢ).
