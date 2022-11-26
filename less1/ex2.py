for x in range(0,2):
    for y in range (0,2):
        for z in range(0,2):
            print(f'x = {x}, y = {y}, z = {z} - {not(x or y or z) == (not x and not y and not z)}')