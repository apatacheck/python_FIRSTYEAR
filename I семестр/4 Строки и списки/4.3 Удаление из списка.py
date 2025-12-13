#Вариант задания - 10
a = input().split()
for i in range(len(a) - 1, -1, -1):
    if len(a[i]) == 3 or (int(a[i]) % 2 != 0):
        del a[i]
print(*a)