def fibo(num):
    if num==0 or num==1:
        return num
    return fibo(num-1)+fibo(num-2)

def negafibo(num):
    return(-1)**(num-1)*fibo(num)

list = []
n = 8

for i in range(n+1):
    list.append(negafibo(i))

list.reverse()
list.pop(-1)

for i in range(n+1):
    list.append(fibo(i))

print(list)