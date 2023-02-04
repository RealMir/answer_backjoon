import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    a = n // 2

    while a > 1:
        if a == 2 : 
            print(2, n-a)
            break
        elif a%2 != 0 :
            for j in range(3,a,2):
                if a%j == 0:
                    break
            else:
                b = n - a
                if b%2 != 0:
                    for j in range(3,b,2):
                        if b%j == 0:
                            break  
                    else:
                        print(a,b)
                        break
        a -= 1