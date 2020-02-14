def IsPointInSquare(x1,y1):
    if -1<=x1<=1 and -1<=y1<=1:
        return True
    return False

a = float(input())
b = float(input())
print(IsPointInSquare(a, b))