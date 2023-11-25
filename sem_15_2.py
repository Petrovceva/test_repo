'''
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК. Соберите 
информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
* имя файла без расширения или название каталога,
* расширение, если это файл,
* флаг каталога,
* название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя логирование.
'''
import os
import sys
import logging
from collections import namedtuple
import argparse


DATA = namedtuple('file_name', '')
def func(lst, path):
    with open(path, 'a', encoding='utf-8') as f:




parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=float, nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'в скрипт передано {args}')

logging.basicConfig(filename='log15_2home.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger('log')

