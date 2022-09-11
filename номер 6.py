# номер 6
k = 0
x = int(input())
while x != 0:
    y = int(input())
    if y > x:
        k = k+1
    x = y
print(k)