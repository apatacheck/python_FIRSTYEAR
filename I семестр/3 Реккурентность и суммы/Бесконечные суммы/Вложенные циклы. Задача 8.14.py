h, e = map(float, input().split())

x = 0.0

while 0.9 + e > x:
    y = 1
    i = 0
    y_sum = 0

    while e < y:
        try:
            y_sum += (-1) ** i * y
            i += 1
            y = x ** i / (2 ** i * 7 * i)

        except OverflowError:
            y_sum = 0
            break

    print(f'{x:.8f}', f'{y_sum:.8f}')
    x += h