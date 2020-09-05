N = int(input())
inp = list(map(int,input().split()))
cnt = 0

for i in range(N):
   
    if inp[i] == 1:
        continue
    elif inp[i] == 2:
        cnt += 1
    elif inp[i] == 3:
        cnt += 1
    else:
         for j in range(2,inp[i]):
            if inp[i] % j == 0:
                break
            elif j == inp[i]-1: # 마지막 까지 돌았다는것을 알려줌
                cnt += 1
                     
print(cnt)
            

            