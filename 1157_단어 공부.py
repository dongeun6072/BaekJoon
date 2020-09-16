inp = input().upper()
inp_list = list(inp)
inp_count = []

for i in inp_list:
    count = inp.count(i)
    inp_count.append(count)

if(inp_count.count(max(inp_count)) >= 2): 
    print("?")
else:
    print(inp_list[(inp_count.index(max(inp_count)))].upper())