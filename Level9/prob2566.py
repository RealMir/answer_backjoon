maxium = 0
row = 0
col = 0
for i in range(9):
    lst = list(map(int, input().split()))
    if max(lst) > maxium:
        maxium = max(lst)
        row = i
        col = lst.index(maxium)
print(maxium)
print(row+1,col+1)