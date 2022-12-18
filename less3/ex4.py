num = 45
res = []
bin = ''
while num > 1:
    res.append(num % 2)
    num = num // 2
res.append(1)
res.reverse()
for i in range(len(res)):
    bin = bin + str(res[i])
print(bin)