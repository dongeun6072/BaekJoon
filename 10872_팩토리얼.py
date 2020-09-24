def factoral(N):
    
    if N <= 1:
        return 1
    else:
        return N * factoral(N-1)


Num = int(input())
print(factoral(Num))