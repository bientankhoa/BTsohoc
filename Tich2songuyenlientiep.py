from math import sqrt

def Ktra(n):
    m = int(sqrt(n))
    i = 1
    while i <= m:
        if n % i == 0 and i * (i+1) == n:
            return True
        i += 1
    return False

k = int(input())
if Ktra(k) == True:
    print("YES")
else:
    print("NO")
