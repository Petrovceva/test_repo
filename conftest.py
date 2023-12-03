import pytest
import yaml
from task_2 import check_command, get_command
import random, string
from datetime import datetime

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture(scope='class')
def make_folders():
    return check_command(f'mkdir -p {data.get('folder_in')} {data.get('folder_out')} {data.get('folder_ex')}')


@pytest.fixture(scope='class')
def delete_folders():
    yield
    return check_command(f'rm -rf {data.get('folder_in')} {data.get('folder_out')} {data.get('folder_ex')}')


@pytest.fixture(scope='class')
def make_files():
    return check_command(f'cd {data.get('folder_in')}; touch file_1.txt file_2.txt file_3.txt, ')


@pytest.fixture(scope='class')
def print_time():
    print("Start: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
    yield
    print("Finish: {}".format(datetime.now().strftime("%H:%M:%S.%f")))


@pytest.fixture(scope='class')
def stat():
    yield
    stat = get_command("cat /proc/loadavg")
    checkout("echo 'time: {} count:{} size: {} load: {}'>> stat.txt".format(datetime.now().strftime("%H:%M:%S.%f"), data["count"], data["bs"], stat), "")
