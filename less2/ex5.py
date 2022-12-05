import time
def randomNum(start, finish):
    now = time.time() % 1
    return int(now * (finish - start) + start)
num = randomNum(-25, 25)
print(num)