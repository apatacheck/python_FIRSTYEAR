from math import *

a, b, h = map(float, input().split())
e = 10 ** -6
while a - b <= e:
    if (a ** 2 - 2 * a + 1) >= 0 and 4 - 2 * a > 0:
        if log(4 - 2 * a) != 0:
            print(f"{a:5f}", f"{(sqrt(a ** 2 - 2 * a + 1)) / log(4 - 2 * a):5f}")
        else:
            print(f"{a:5f}", "undefined")
    else:
        print(f"{a:5f}", "undefined")
    a = float(f"{a + h:5f}")