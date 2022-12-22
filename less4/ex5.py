str1 = ""
str2 = ""

with open('less4-5-1.txt', 'r') as file:
    for line in file:
        str1 = line

with open('less4-5-2.txt', 'r') as file:
    for line in file:
        str2 = line

print(str1)
print(str2)        

str1 = str1[0:-4]
str2 = str2[0:-4]
str1 = str1.replace(" - "," + -")
str2 = str2.replace(" - "," + -")
str1_list = str1.split(" + ")
str2_list = str2.split(" + ")

def d(str_list):
    d = {}
    for i in range(len(str_list)):
        if str_list[i].count("x^"):
            d[int(str_list[i].split("^")[1])] = int(str_list[i].split("*")[0])
        elif str_list[i].count("x"):
            d[1] = int(str_list[i].split("*")[0])
        else:
            d[0] = int(str_list[i])
    return d        

d1 = d(str1_list)
d2 = d(str2_list)

print(d1)
print(d2)

max_index = 0
for key in d1.keys():
    if max_index < key:
        max_index = key
for key in d2.keys():
    if max_index < key:
        max_index = key


d3 = {}
for i in range(max_index, -1, - 1):
    if i in d1:
        if i in d2:
            d3[i] = d1[i] + d2[i]
        else:
            d3[i] = d1[i]
    elif i in d2:
        d3[i] = d2[i]     
print(d3)

final = []
for i in range(max_index, -1, - 1):
    if i in d3:
        if i == 1:
            final.append(str(d3[i]) + "*x")
        elif i == 0:
            final.append(str(d3[i]))
        else:
            final.append(str(d3[i]) + "*x^" + str(i))

final_text =  ' + '.join(final)    
final_text = final_text.replace(" + -"," - ")

with open('less4-5.txt', 'a') as file:
    print(final_text, file=file, end=' = 0\n')