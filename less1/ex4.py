q = int(input('Введите номер четверти:'))
if 1 <= q <= 4:
    if q==1:
        print('x > 0, y > 0')
    elif q==2:
        print('x < 0, y > 0')
    elif q==3:
        print('x < 0, y < 0')
    elif q==4:
        print('x > 0, y < 0')
else:
    print('Нет такой четверти')
