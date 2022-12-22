import random
k = 6
c = [random.randint(-100,100) for i in range(0,k+1)]
print(c)

def Pol(k,c):
    p = ''
    for i in range(0, k+1):
        if c[i] == 0:
            pol += ''  
        elif k - i > 1:
            p += f'{c[i]} * x^{k - i} + '
        elif k - i  == 1:
            p += f'{c[i]} * x + '   
        else:
            p+= f'{c[i]} = 0'
    return p

with open ('less4-p.txt', 'w') as data:
    data.write(Pol(k,c).replace('+ -','- '))

