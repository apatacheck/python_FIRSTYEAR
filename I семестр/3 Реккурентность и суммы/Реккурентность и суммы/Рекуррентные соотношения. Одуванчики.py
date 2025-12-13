m, n = map(int, input().split())
w = m // 2
day = 0
mc = 0
wc = 0

while (mc + wc) < n:
    day += 1
    mc += m
    wc += w
    if (mc + wc) >= n:
        break
    m = int(m - m * 0.1)
    if m < 0:
        m = 0
    w = int(w + w * 0.15)
    if w < 0:
        w = 0
    if m == 0 and w == 0:
        break

if mc + wc < n:
    print(0, int(mc), int(wc))
else:
    print(day, int(mc), int(wc))