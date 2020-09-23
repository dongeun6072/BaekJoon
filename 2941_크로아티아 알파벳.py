a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
num = input()
for i in a:

    num = num.replace(i, 'a')
    
print(len(num))