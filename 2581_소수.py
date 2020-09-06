M = int(input())
N = int(input())
oup = []
for i in range(M,N+1):
    
    if i == 2:
        oup.append(i)

    else:
        for j in range(2,i):
            if i % j == 0:
                break
            elif j == i - 1:
             oup.append(i)

if len(oup) == 0:
    print(-1)
else:
    print(sum(oup))
    print(min(oup))



    