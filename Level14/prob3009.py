import sys

def f(lst):
    for i in lst:
        cnt = lst.count(i)
        if cnt == 1:
            print(i,end=" ")
            break

lst = [None]*3
lst2 = [None]*3

for i in range(3):
    lst[i], lst2[i] = map(int,sys.stdin.readline().split())
    
f(lst)
f(lst2)