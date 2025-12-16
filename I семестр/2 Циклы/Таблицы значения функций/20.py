from math import *
a, b, h = map(float, input().split())
while a <= b:
    if a != -7 and 1 - abs(a) > 0:
        print(f"{a:5f}", f"{(1/(a+7))+(log(1-abs(a))):5f}")
    else:
        print(f"{a:5f}", "undefined")
    a = float(f"{a+h:5f}")