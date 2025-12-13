a, b, h = map(float, input().split())
e = 10 ** -6
while a - b <= e:
    if abs((a ** 3) + 8) != 0:
        print(f"{a:5f}", f"{3 / abs((a ** 3) + 8):5f}")
    else:
        print(f"{a:5f}", "undefined")
    a = float(f"{a + h:5f}")