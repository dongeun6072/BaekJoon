num = set(range(1,10001))
generated_num = set()
for i in range(1,10001):
    print(i)
    for j in str(i):
        print("{0} {1}".format(int(j),i))
        i += int(j)
    generated_num.add(i)
self_num = num - generated_num
for k in sorted(self_num):
    print(k)