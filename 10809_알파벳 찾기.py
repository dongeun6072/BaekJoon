alphabet = "abcdefghijklmnopqrstuvwxyz"
N = input()

Wd_num = []
num = []

for i in N:
    Wd_num.append(i)

for i in alphabet:
   
    for j in range(len(Wd_num)):
        if i == Wd_num[j]:
           num.append(j)
           break
        elif j < len(Wd_num)-1: continue
        else:
            num.append(-1)
        
for i in num:
    print(i,end=" ")







