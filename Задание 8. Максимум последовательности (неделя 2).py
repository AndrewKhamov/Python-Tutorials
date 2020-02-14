#a = int(input('Vvedite element posledovatelnosti: '))
now = int(input())
nowMax = now
while now !=0:
    now = int(input())
    if now > nowMax:
        nowMax = now
print(nowMax)