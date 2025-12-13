#Вариант задания: 6
c = 0
with open('lines.txt', 'r') as f:
    nums = f.read().splitlines()
for i in range(len(nums)):
    a = nums[i].split()
    for z in range(len(a) - 1, -1, -1):
        if len(a[z]) > 3:
            c += 1
if c == 0:
    print('НЕТ')
else:
    print('ДА')
