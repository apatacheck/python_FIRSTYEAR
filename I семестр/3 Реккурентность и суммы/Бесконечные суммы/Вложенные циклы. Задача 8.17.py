h, e = map(float, input().split())
x = 0.0
while 0.8 + e > x:
    y = 1
    c1 = 0
    c2 = 1
    c3 = 3
    y1 = 0
    while e < y:
        y1 += (-1) ** c1 * y  # периодичность знака
        c1 += 1
        c2 += 2
        y = x ** c2 / (c3 * (c3 + 1) ** 2)
        c3 += 1
    if c2 == 10000:
        y = 0.0
        print(f'{x:.8f}', f'{y:.8f}')
        break
    print(f'{x:.8f}', f'{y1:.8f}')
    x += h