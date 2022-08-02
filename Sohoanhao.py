from math import sqrt

def tonguoc(k):
    s = 0
    for i in range(1,int(sqrt(k))+1):
        if k % i == 0:
            s = s + i
            j = k // i
            if j != i:
                s = s + j
    if (s - k) == k:
        return True
    else:
        return False

n = int(input())
if tonguoc(n) == True:
    print("YES")
else:
    print("NO")