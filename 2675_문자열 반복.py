T = int(input())

for i in range(T):
    rep, num = input().split()
    rep = int(rep)
    num = str(num)
    for i in range(len(num)):
        print("{0}".format(num[i] * rep),end="")
    print()