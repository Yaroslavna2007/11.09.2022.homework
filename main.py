# номер 1
x = input().split()
k = 0
for s in range(1,len(x)-1):
    if (x[s] > x[s-1]) and (x[s] > x[s+1]):
        k = k+1
print(k)