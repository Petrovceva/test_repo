# дом.задание1

# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print('Введите трехзначное число: ')
a = int (input())
sum = 0
while a > 0:
    sum = sum + a%10
    a = a//10
print('сумма чисел равна: ', sum)
