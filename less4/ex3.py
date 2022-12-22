posl = [1,1,2,4,4,4,4,5,6,6,6,6,7,7,8]
for i in posl:
    c = posl.count(i)
    if(c) > 1:
        while c > 1:
            posl.remove(i)
            c -= 1
print(posl)       