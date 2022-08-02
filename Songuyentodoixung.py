from math import sqrt

def doixung(a):
    s = 0
    b = a
    while b > 0:
        du = b % 10
        s = s * 10 + du
        b = b // 10
    if s == a:
        return True
    else :
        return False

def songuyento(n):
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0 or n % 3 == 0:
        return False 
    i = 5
    while i <= int(sqrt(n)):
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

m = int(input())
if doixung(m) == True:
    if songuyento(m) == True:
        print("Y")
        exit()

print ("N")
