def Tongcs(a):
    s = 0
    while a > 0:
        du = a % 10
        s = s + du
        a = a // 10
    return s

def soluong(b):
    d = 0
    while b > 0:
        du = b % 10
        d = d + 1
        b = b // 10
    return d

m = int(input())
t = soluong(m)
for x in range((m-t*9),m+1):
    if x + Tongcs(x) == m:
        print(x)
        break
