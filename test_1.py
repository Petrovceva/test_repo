import pytest
import yaml

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load()


def test_step_1(site, select_input_login, select_input_password, select_input_button, select_error):
    input1 = site.find_element("xpath", select_input_login)
    input1.send_keys("test")
    input2 = site.find_element("xpath", select_input_password)
    input2.send_keys("test")
    btn = site.find_element("css", select_input_button)
    btn.click()
    err_label = site.find_element("xpath", select_error)
    assert err_label.text == "401"


def test_step_2(site, select_input_login, select_input_password, select_input_button, select_hello_user):
    input1 = site.find_element("xpath", select_input_login)
    input1.send_keys("test")
    input2 = site.find_element("xpath", select_input_password)
    input2.send_keys("test")
    btn = site.find_element("css", select_input_button)
    btn.click()
    answer = site.find_element('xpath', select_hello_user)
    assert answer.text == f'Hello, {testdata["login"]}'
