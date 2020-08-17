Test = int(input())

for i in range(Test):
    n = list(map(int,input().split()))
    sum = 0
    cnt = 0
    for j in n[1:]:
        sum = sum + j
        
    pre_avg = sum / n[0] 
    
    for j in n[1:]:
        if j > pre_avg:
            cnt = cnt + 1   
      
    print("%0.3f" % (cnt/n[0]*100) + '%')  
    
 