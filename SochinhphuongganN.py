from math import sqrt

n = int(input())

k = int(sqrt(n))

if abs(k**2 - n) > (k+1) ** 2 - n:
    print((k+1)**2)
else:
    print(k**2)