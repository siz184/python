
number = int(input('Number: '))
product = 0
sum = 0
i = 1
plist = []
while i <= number:
    product = round((1 + (1/i)) ** i,3)
    plist.append(product) 
    sum += product
    i += 1
print(plist)
print(sum)