N = int(input())
x = 0
sum = 0 
while True:
    if (N % 5) == 0:
        sum += N // 5
        print(sum)
        break
    
    N = N - 3
    sum += 1

    if N < 0:
        print(-1)
        break
    