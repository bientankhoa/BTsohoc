e = [0 for i in range(1000001)]

def sang():
    e[0] = e[1] = 1
    j = 2
    while j**2 <= 1000001:
        if e[j] == 0:
            for x in range(j*j,1000001,j):
                e[x] = 1
        j += 1

def nhiphan(n):
    s = 0
    while n > 0:
        du = n % 2
        s = s + du
        n = n // 2
    return s
        
sang()
dem = 0

a = [int(i) for i in input().split()]
n,h = a[0],a[1]
for i in range(10,n+1):
    if e[i] == 0 and nhiphan(i) == h:
        dem += 1

print (dem)