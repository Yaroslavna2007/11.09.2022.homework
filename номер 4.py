# номер 4
m = -12345
x = int(input())
i = -1
while x != 0:
    if x > m:
        m = x
        i = i+1
    x = int(input())
print(i)