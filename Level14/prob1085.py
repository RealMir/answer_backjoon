import sys
x,y,w,h = map(int, sys.stdin.readline().split())
print(min(x,y,w-x,h-y))