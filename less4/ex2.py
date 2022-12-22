n = 12345
d = 2
list_mn = []
while n > 1:
    if n % d == 0:
        list_mn.append(d)
        n = int(n / d)
    else:
        d += 1

print(*list_mn, sep = " * ")
