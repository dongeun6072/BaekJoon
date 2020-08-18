def Hannum(n):

    cnt = 0

    if n < 100:
        return n

    else:
        for i in range(100,(n+1)):
             fir = (i % 100) % 10
             sec = (i % 100) // 10
             thi = i // 100
             if (sec-thi) == (fir-sec):
                cnt += 1

        return 99 + cnt  

num = int(input())
res = Hannum(num)
print(res)
    
    
    
    
    
                     