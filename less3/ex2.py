list = [2, 3, 4, 5, 6]
i=0
h=len(list)//2
prod = []
while i < h:
    prod.append(list[i]*list[-i-1])
    i+=1
prod.append(list[i]**2)
print(prod)