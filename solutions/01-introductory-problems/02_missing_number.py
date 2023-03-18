# https://cses.fi/problemset/task/1083

n = int(input())
a = [int(x) for x in input().split()]

print(sum(range(1, n + 1)) - sum(a))