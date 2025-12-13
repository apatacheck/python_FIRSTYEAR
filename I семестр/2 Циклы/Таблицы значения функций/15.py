from math import *

a, b, h = map(float, input().split())
e = 10 ** -6
while a - b <= e:
    if (2 * (a ** 5) - 1) > 0:
        if (abs(3 * a) * sqrt(2 * (a ** 5) - 1)) != 0:
            print(f"{a:5f}", f"{log(abs(3 * a)) * sqrt(2 * (a ** 5) - 1):5f}")
        else:
            print(f"{a:5f}", "undefined")
    else:
        print(f"{a:5f}", "undefined")
    a = float(f"{a + h:5f}")