a, b = map(int, input().split())
a1 = a2 = a
n0 = 1
n1 = 1
summ = a2
while summ < 1000000:
    a2 = a2 * 3
    summ += a2
    n1 += 1
while a1 < b:
    a1 = a1 * 3
    n0 += 1
print(n0, n1)