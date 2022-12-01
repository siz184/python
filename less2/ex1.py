
number = input('Number: ')
sum = 0
for c in number:
    if c.isdigit():
        sum += int(c)
print(f'Sum: {sum}')