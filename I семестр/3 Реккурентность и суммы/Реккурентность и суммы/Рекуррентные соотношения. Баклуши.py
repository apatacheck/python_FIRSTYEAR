a, m = map(int, input().split())
s = sums = a
v = sumv = a * 1.3
n = 1
while sumv + sums < m:
    s += 6
    v = s * 1.3
    sumv += v
    sums += s
    n += 1
print(n, sums)