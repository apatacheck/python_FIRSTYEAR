n, m = map(int, input().split())
summa = 0
dlina = 0
for i in range(n):
    inp = list(map(int, input().split()))
    summa += sum(inp)
    dlina += len(inp)
    sr = summa / dlina
print(sr)