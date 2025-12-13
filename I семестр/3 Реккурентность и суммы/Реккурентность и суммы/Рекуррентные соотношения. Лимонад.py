s, k, m = map(int, input().split())
answ = 0
while s >= k:
    answ += 1
    s = s - k + m
print(answ)