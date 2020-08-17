N = int(input())

for i in range(N):
  Test = list(input())
  cnt = 0
  sum = 0
  for i in Test:
     if i == 'O':
        cnt = cnt + 1
     else:
        cnt = 0
     sum = sum + cnt 
  print(sum)  
      