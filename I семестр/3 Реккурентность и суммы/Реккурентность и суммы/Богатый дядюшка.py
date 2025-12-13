import math


def f(n):
    if n == 1:
        return 1
    else:
        return (f(n - 1)) * 2 + n


summ = 0
n = int(input())
for i in range(1, n + 1):
    summ += f(i)
if summ == 0:
    summ = 1
print(summ)