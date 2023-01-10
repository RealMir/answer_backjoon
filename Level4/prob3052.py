import sys

lst = []
cnt = 0
for _ in range(10):
  b = int(sys.stdin.readline()) % 42
  if b not in lst:
    cnt += 1
  lst.append(b)
print(cnt)