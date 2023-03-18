# https://cses.fi/problemset/task/1070

n = int(input())

if n == 1:
    print(1)
elif n <= 3:
    print("NO SOLUTION")
else:
    print(*range(n - 1, 0, -2), *range(n, 0, -2))
