import sys

lst = []
for _ in range(9):
  lst.append(int(sys.stdin.readline()))
maxium = max(lst)
print(f"{maxium}\n{lst.index(maxium)+1}")
