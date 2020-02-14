a = int(input('Pervaya kvartira v pod.ezde: '))
b = int(input('Poslednyaia kvartira v pod.ezde: '))
if b>a:
    if (a-1) % (b-a+1) == 0:
        print('Yes')
    else:
        print("No")
else:
    print("Error")
# a-1 % b-a+1
