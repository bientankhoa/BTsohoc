c = [int(i) for i in input().split()]
a,b = c[0],c[1]
m = max(a,b)
d = 0

while d == 0:
    if (m + a) % b == 0 and (m + b) % a == 0:
        print(m)
        break
    m += 1