n = int(input())
listOfVillages = list(map(int, input().split()))
listOfVillages.sort()
villages = []
for i in range(n):
    village = (int(i), listOfVillages[i])
    villages.append(village)
print(villages)
m = int(input())
listOfShelters = list(map(int, input().split()))
shelters = []
listOfShelters.sort()
for i in range(m):
    shelters.append((int(i), listOfShelters[i]))
print(shelters)
b = 1
ansList = []
for i in range(n):
    min = abs(villages[i][1] - shelters[0][1])
    ans = shelters[0][0]
    pos = 1
    for j in range(b, m):
        if abs(villages[i][1] - shelters[j][1]) < min:
            min = abs(villages[i][1] - shelters[j][1])
            ans = shelters[j][0]
            pos = j
        else:
            break
    ansList.append(ans + 1)
    b = pos
print(ansList)

# не обращай внимания.
