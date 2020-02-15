a = list(map(int, input().split()))
aMax = 0
for i in range(len(a)):
    if a[i] >= aMax:
        aMax = a[i]
        iMax = i
print(aMax, iMax)
