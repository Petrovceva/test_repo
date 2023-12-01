'''Задание 1.
Условие:
Написать функцию на Python, которой передаются в качестве параметров команда и текст. Функция должна возвращать True, 
если команда успешно выполнена и текст найден в её выводе и False в противном случае. Передаваться должна только одна 
строка, разбиение вывода использовать не нужно.

Задание 2. (повышенной сложности)
Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы, 
в котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять из списка string.punctuation 
модуля string). В этом режиме должно проверяться наличие слова в выводе.
'''


import subprocess
import string


def execute_command(command, text, punctuation_mode=False):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if process.returncode == 0:
        if punctuation_mode:
            words = output.decode().split()
            words = [word.strip(string.punctuation) for word in words]
            return text in words
        else:
            return text in output.decode()
    return False
