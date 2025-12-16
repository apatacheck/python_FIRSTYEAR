h, e = map(float, input().split())

x = 0.6

while 1.0 + e > x:
    y0 = x
    y1 = x ** 2 / 10
    i = 1
    y_sum = y0 + y1

    while e < y1:
        try:
            y0, y1 = y1, 2 * x * y1 ** 2 - y0 ** 3 * x ** 4
            y_sum += y1
            i += 1
        except OverflowError:
            y_sum = 0
            break

    print(f'{x:.8f}', f'{y_sum:.8f}')
    x += h