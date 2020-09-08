import math

def Dis(num):
    a = int(math.sqrt(num))

    if num == 1:
        return False
    else:
        for i in range(2, a+1):
            if num % i == 0: 
                return False
        return True

m,n = map(int,input().split())
for i in range(m,n+1):
    if Dis(i):
        print(i)
