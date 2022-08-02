c = [int(i) for i in input().split()]
a,b = c[0],c[1]
i,j,t1,t2 = 2,2,2,2
d = []
e = []

while a > 1:
    if a % i == 0:
        if i != t1:
            d.append(i)
        t1 = i
        a = a / i
    else:
        i += 1

while b > 1:
    if b % j == 0:
        if j != t2 :
            e.append(j)
        t2 = j
        b = b / j
    else:
        j += 1

if d == e:
    print("YES")
else :
    print("NO")