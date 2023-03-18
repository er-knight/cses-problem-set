# https://cses.fi/problemset/task/1069

s = input()

i, l, m = 1, 1, 1
while i < len(s):
    if s[i] == s[i - 1]:
        l += 1
    else:
        l = 1
    i += 1
    m  = max(m, l)

print(m)