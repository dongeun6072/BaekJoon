N = int(input())
human_list = []
for i in range(N):
    x,y = map(int,input().split())
    human_list.append((x,y))

for i in human_list:
    level = 1
    for j in human_list:
        if i[0] < j[0] and i[1] < j[1]:
            level += 1
    print(level, end=" ")


        
    
    