# дом.задание1

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое 
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

print ('Введите число, кратное 6: ')
s = int(input())
a = int(s/6)
b = int(s/6*2*2)

print ('Петя и Сережа сделали по ', a, 'корабликов, ', 'Катя сделала ', b, 'корабликов')
