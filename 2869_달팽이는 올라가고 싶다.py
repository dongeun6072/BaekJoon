A,B,V = map(int,input().split())

hig = V-A
if hig % (A-B) == 0:
    cnt = int(hig/(A-B))
else:
    cnt = int(hig/(A-B)+1)

print(cnt+1)