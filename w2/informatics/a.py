# https://informatics.msk.ru/mod/statements/view.php?id=2741#1

arr = list(map(int, input().split()))

for i in range(0, len(arr)):
    if i % 2 == 0:
        print(arr[i], end=' ')

