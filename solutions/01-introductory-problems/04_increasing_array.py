# https://cses.fi/problemset/task/1094

n = int(input())
a = [int(x) for x in input().split()]

i, m = 1, 0
while i < n:
    if a[i] < a[i - 1]:
        m += (a[i - 1] - a[i])
        a[i] = a[i - 1]
    i += 1
    
print(m)
