import math

def IsPrime(num):
    a = int(math.sqrt(num))
    if num == 1:
        return False
    else:
        for i in range(2, a+1):
            if num % i == 0: 
                return False
        return True

Num_list = list(range(2,246912))
Sort_list = []
for i in Num_list:
    if IsPrime(i):
         Sort_list.append(i)

T = int(input())
for i in range(T):
    N = int(input())
    oup = []    
    for j in Sort_list:
        if N >= j:
           oup.append(j) 
    print(oup)

    for i in oup:
        for j in oup:
            if N == i+j:
                print("{0} + {1} = {2}".format(i,j,i+j))
        