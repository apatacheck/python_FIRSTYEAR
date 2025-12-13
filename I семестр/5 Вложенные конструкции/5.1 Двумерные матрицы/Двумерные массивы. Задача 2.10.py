n, m = map(int, input().split())
s = [list(map(int, input().split())) for i in range(n)]
s1 = list(zip(*s))  # объединение в одномерный массив
print(*[min(i) for i in s1])