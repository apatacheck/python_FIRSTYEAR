s = int(input())
a = b = c = 100
for i in range(2, s):
    c = a + b
    a = b
    b = c
print(f"{c/1000:.1f}")