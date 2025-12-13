h, e = map(float, input().split())
x = 0.1
while 0.9 + e > x:
    y = 1 + x / 4
    c1 = 0
    c2 = 1
    y1 = 0
    while e < y:
        y1 += (-1) ** c1 * y  # периодичность знака
        c1 += 1
        c2 += 1
        y = x ** c2 / (c2 * (c2 + 3))
    if c2 == 10000:
        y = 0.0
        print(f'{x:.8f}', f'{y:.8f}')
        break
    print(f'{x:.8f}', f'{y1:.8f}')
    x += h