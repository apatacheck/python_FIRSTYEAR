from math import *
a, b, h = map(float, input().split())
while a <= b:
    x = a
    if ((x ** 4) - 1) > 0 and (1 + x) > 0:
        print(f"{x:5f}", f"{log((x ** 4) - 1)*log(1 + x):5f}")
    else:
        print(f"{x:5f}", "undefined")
    a = float(f"{a + h:5f}")