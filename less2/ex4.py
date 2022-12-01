number = int(input('Number: '))
sum = 1
nlist = []
plist = []

for i in range(-abs(number), abs(number) + 1):
    nlist.append(i) 
    
print(nlist)

positions = 'file.txt'
with open(positions, 'r') as data:
    for position in data:
        plist.append(int(position))

print(plist)

for p in plist:
    sum *= nlist[p]

print(sum)   