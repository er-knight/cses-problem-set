t = int(input())
for i in range(t):
    y, x = [int(x) for x in input().split()]
    if y > x:
        if y % 2 == 0:
            print(y ** 2 - (x - 1))
        else:
            print((y - 1) ** 2 + x)
    else:
        if x % 2 == 0:
            print((x - 1) ** 2 + y)
        else:
            print(x ** 2 - (y - 1))

