a,b = map(int,input().split())
m = list(map(int,input().split()))
num_list = []
sum = 0
n = len(m)

for i in range(n-2):
    for j in range(i+1,n-1):
        for l in range(j+1,n):
            sum = m[i] + m[j] + m[l]
            if (sum <= b):
                num_list.append(sum)
        
print(max(num_list))


    