import math
import sys

while 1:  
    n = int(sys.stdin.readline())

    if n == 0:
        break

    end = n*2
    m = int(math.sqrt(end))

    lst = [False,False]+[True]*(end-1)
    prime = []

    for i in range(2,m+1,1):
        if lst[i]:
            prime.append(i)
            for j in range(2*i,end+1,i):
                lst[j] = False

    lst[:n+1] = [False]*(n+1)
    print(lst.count(True))