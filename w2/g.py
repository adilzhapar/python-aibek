arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(0, len(arr)):
    print(arr[i], end=' ')

print()

for i in range(0, len(arr)):
    arr[i] *= 10


for i in arr:
    print(i, end=' ')