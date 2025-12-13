n, m = map(int, input().split())
s = [list(map(int, input().split()))[::-1] for i in range(n)]
for answ in s:
    print(*answ)