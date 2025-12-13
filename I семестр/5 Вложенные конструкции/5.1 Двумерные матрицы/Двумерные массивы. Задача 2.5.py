n = int(input())
summa = 0
dlina = 0
for i in range(n):
    inp = list(map(int, input().split()))
    s = inp[-(i + 1):][1:]
    summa += sum(s)
    dlina += len(s)
if dlina == 0:
    print('No')
else:
    print(f'{(summa / dlina):.6f}')