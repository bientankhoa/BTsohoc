from math import sqrt

n = int(input())

t = int(sqrt(n))

if t ** 2 == n:
    print("YES")
else:
    print("NO")