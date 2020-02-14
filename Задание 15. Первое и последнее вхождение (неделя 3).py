a = 'offensife'
pos = (a.find('f'))
while pos != -1:
    print(pos)
    pos = a.find('f', pos+1)
