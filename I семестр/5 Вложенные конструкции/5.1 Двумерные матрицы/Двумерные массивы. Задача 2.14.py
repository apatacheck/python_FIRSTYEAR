n, m = map(int, input().split())
s = [list(map(int, input().split())) for i in range(n)]
if n % 2 == 0:
    s = [i for numbers in zip(s[1::2], s[::2]) for i in numbers]
for answ in s:
    print(*answ)