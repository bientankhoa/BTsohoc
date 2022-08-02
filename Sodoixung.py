def sodoixung(n):
    k = n
    s = 0
    while k > 0:
        du = k % 10
        s = s * 10 + du
        k = k // 10
    
    if s == n:
        return True
    else:
        return False

m = int(input())
if sodoixung(m) == True:
    print("Y")
else:
    print("N")