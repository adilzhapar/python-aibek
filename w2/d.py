a = int(input())

# if (a is even) AND (a is postive):
if a % 2 == 0 and a > 0:
    print('even postive')

# 5 // 2 = 2
# 5 % 2 = 1

s = input()

if s == 'Almaty' or s == 'Taraz':
    print('tigr')
else:
    print('lame')

# SAME AS:

if s == 'Almaty':
    print('tigr')
elif s == 'Taraz':
    print('tigr')
else:
    print('lame')

    