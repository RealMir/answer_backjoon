import sys

n = 5
x = [None]*n
for i in range(n):
   x[i] = int(sys.stdin.readline())

k = 0
while k < n-1:
    last = n-1
    for i in range(n-1,k,-1):
        if x[i] < x[i-1]:
            x[i], x[i-1] = x[i-1], x[i]
            last = i
    k = last

print(sum(x)//n)
print(x[2])