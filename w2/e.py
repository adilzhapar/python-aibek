# вывести все числа от 1 до n inclusevely

n = int(input())

# [1, 10 + 1)
for i in range(1, n + 1):
    print(i, end=' ')

print() # new line

i = 1
while i <= n:
    print(i, end=' ')
    i += 1

