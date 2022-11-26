num = int(input('Введите цифру от 1 ло 7: '))
if 1 <= num <= 7:
    if 6 <= num <= 7:
        print(f'{num} - выходной')
    else:
        print(f'{num} - не выходной')
else:
    print(f'{num} - не номер дня недели')