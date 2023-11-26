''''
- функция получает на вход текст вида: "1-й четверг ноября", "3-я среда мая" и т.п.
- верните дату в текущем году, соответствующую этому тексту.
Логируйте ошибки, если текст не соответствует формату.
- логгируйте объект именованного кортежа с атрибутами, соответствующими дате,
если дата существует.

Дорабатываем задачу 4. Добавьте регистрацию возможных ошибок. Добавьте возможность запуска 
из командной строки с использованием библиотеки argparse.
'''
import os
import logging
import datetime
from datetime import date, datetime
from collections import namedtuple
import argparse

parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('numbers', metavar='N', type=str, nargs='*', help='press some numbers')
args = parser.parse_args()
print(f'в скрипт передано {args}')

logging.basicConfig(filename='log15_home.log', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger('log')

MONTH = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12
}
WEEKDAYS = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6
}

DATE = namedtuple("DATE", "day month year")

def get_date(text):
    num_week, week_day, mounth = text.split()
    num_week = int(num_week.split("-")[0])
    week_day = WEEKDAYS[week_day]
    count_week = 0
    for day in range(1, 31+1):
        d = date(year=datetime.now().year, month=MONTH[mounth], day=day)
        if d.weekday() == week_day:
            count_week += 1
            if count_week == num_week:
                logger.info(DATE(d.day, d.month, d.year))
                return d

print(get_date(input('введите текст вида: "1-й четверг ноября" ')))
        
