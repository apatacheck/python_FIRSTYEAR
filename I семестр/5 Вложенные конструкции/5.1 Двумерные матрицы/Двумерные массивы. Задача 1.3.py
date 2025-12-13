n, m = map(int, input().split())
A, B = map(int, input().split())
answ = []
for i in range(n):
    inp = list(map(int, input().split()))
    if any(A <= x <= B for x in inp):
        inp = [0 if A <= number <= B else number for number in inp]
    answ.append(inp)
for inp in answ:
    print(*inp)