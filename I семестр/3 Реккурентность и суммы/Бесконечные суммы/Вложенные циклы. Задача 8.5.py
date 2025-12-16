h, e = map(float, input().split())

x = 0.05

while 0.95 + e > x:
    y = 1
    i = 0
    i1 = 1
    i2 = i1
    y_sum = 0

    while e < y:
        y_sum += (-1) ** i * y
        i += 1
        i2 += 2
        i1 *= i2
        y = x ** i / i1

    print(f'{x:.8f}', f'{y_sum:.8f}')
    x += h