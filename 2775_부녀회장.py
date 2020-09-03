T = int(input())

for i in range(T):
     d = []
     k = int(input())
     n = int(input())
     d = [j for j in range(1, n+1)]
    
     for i in range(k):
         for j in range(1,n):
              d[j] += d[j-1]

     print(d[n-1])

