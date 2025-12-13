n, m = map(int, input().split())
k = int(input())
s = []
for num in range(n):
    inp = list(map(int, input().split()))
    if any(num > k for num in inp):
        for i in range(len(inp)):
            if inp[i] > k:
                s.append([num + 1, i + 1])  # num+1 - номер элемента,i+1 - индекс элемента
for answ in s:
    print(answ[0], answ[1])