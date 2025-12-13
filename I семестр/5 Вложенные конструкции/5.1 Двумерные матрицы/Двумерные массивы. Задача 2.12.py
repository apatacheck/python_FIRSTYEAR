n, m = map(int, input().split())
s = [list(map(int, input().split())) for i in range(n)]
if n % 2 != 0:
    s[0], s[n // 2] = s[n // 2], s[0]
else:
    s[n // 2 - 1], s[n // 2] = s[n // 2], s[n // 2 - 1]
for answ in s:
    print(*answ)