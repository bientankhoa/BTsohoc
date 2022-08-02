def sodep(n):
    s = 0
    while n > 0:
        du = n % 10
        s = s + du
        n = n // 10
    
    if s % 10 == 9:
        return True
    else :
        return False

m = int(input())
if sodep(m) == True:
    print ("YES")
else:
    print("NO")