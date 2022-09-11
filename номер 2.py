# номер 2 не получилось:(
x = input().split()
m = 0
for s in range(1,len(x)):
    x[s] = int()
    x[m] = int()
    if x[s] > x[m]:
        m = x[s]
print(x[m],m)