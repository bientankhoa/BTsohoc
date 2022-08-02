def tongso(n):
    s = 0
    k = n
    while n > 0:
        du = n % 10
        s = s + du
        n = n // 10
    if k % s == 0:
        return True
    else :
        return False

m = int(input())
if tongso(m) == True:
    print("Y")
else :
    print ("N")