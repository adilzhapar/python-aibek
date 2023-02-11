# if every digit is in new line
n = int(input())

arr = []
for i in range(0, n):
    x = int(input())
    arr.append(x)

# for i in l:
#     print(i, end=' ')
print(*arr)