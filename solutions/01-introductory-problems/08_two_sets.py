# https://cses.fi/problemset/task/1092

n = int(input())
s = int(n * (n + 1) / 2)
if s % 2 == 0:
    print("YES")
    a, b, s = [], [], int(s / 2)
    for i in range(n, 0, -1):
        if s >= i:
            a.append(i)
            s -= i
        else:
            b.append(i)
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)
else:
    print("NO")
