n = int(input())
room = sum = 1
while sum < n:
  sum += room * 6
  room += 1
print(room)