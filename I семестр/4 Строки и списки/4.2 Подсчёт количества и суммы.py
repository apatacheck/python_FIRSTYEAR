#Вариант задания: 14
def stepeni(num, k):
    count = num
    while count % k == 0:
        count /= k

    return count == 1


def neubivanie(num):
    num_str = str(num)
    for i in range(len(num_str) - 1):
        if num_str[i] > num_str[i + 1]:
            return False
    return True


c = 0
summ = 0
a = list(map(int, input('Введите числа через запятую:\n').split(',')))
start = int(input('Начало: '))
stop = int(input('Конец: '))
for i in range(start-1, stop):
    if neubivanie(a[i]):
        c += 1
        if ('3' in str(a[i])) and (stepeni(a[i], 3) == 1):
            summ += a[i]
print(f'Количество:{c},Сумма:{summ}')