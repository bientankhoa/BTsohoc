from math import sqrt
n = int(input())

k = int(sqrt(2*n))

s = ((k + 1) * k) // 2

if s == n:
    print("YES")
else :
    print ("NO")