n = int(input())
summa, dlina = 0, 0
for i in range(n):
    inp = list(map(int, input().split()))
    if any(inp[j] % 2 != 0 for j in range(i + 1, len(inp))):
        for j in range(i + 1, len(inp)):
            if inp[j] % 2 != 0:
                summa += inp[j]
                dlina += 1
if dlina == 0:
    print('No')
else:
    print(f'{(summa / dlina):.6f}')