import sys
while 1:
    num = list(map(int, sys.stdin.readline().split()))

    if num == [0,0,0]:
        break

    maxium = max(num)
    num.remove(maxium)

    if num[0]**2 + num[1]**2 == maxium**2:
        print("right")
    else:
        print("wrong")