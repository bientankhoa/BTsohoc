from math import sqrt
def songuyento(n):
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i <= sqrt(n):
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

m = int(input())
if songuyento(m) == True:
    print("Y")
else :
    print("N")