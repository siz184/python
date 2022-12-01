
number = int(input('Number: '))
product = 1
i = 1
plist = []
while i <= number:
    product *= i
    plist.append(product) 
    i += 1
print(plist)