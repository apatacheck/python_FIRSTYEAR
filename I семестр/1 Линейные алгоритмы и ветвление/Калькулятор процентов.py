print("Введите число: ")
number = float(input())
print("Выберите действие: ", "1.Найти процент от введённого числа ", "2.Увеличить число на какой-то процент",
      "3.Уменьшить число на какой-то процент", sep='\n')
action = int(input())
while (action != 1) and (action != 2) and (action != 3):
    print("Данного действия нет в списке,выберите действие из списка: ", "1.Найти процент от введённого числа ",
          "2.Увеличить число на какой-то процент", "3.Уменьшить число на какой-то процент", sep='\n')
    action = int(input())
print('Введите значение процента:')
precent = float(input())
while precent <= 0:
    print('Процент введен некорректно,повторите попытку:')
    precent = float(input())
if action == 1:
    answer = number * (precent / 100)
if action == 2:
    answer = number + (number * (precent / 100))
if action == 3:
    answer = number - (number * (precent / 100))
print(f'Ответ:{answer}')