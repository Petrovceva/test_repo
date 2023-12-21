from testpage import OperationsHelper
import logging
import yaml
import time

with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_step_1(browser):
    logging.info("Test1 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'

def test_step_2(browser):
    logging.info("Test2 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    assert testpage.get_success_text() == f'Hello, {testdata["login"]}'
   
def test_step_3(browser):
    logging.info("Test3 starting")
    testpage = OperationsHelper(browser)
    testpage.click_new_post_btn()
    testpage.enter_title("testtitle")
    testpage.enter_content("testcontent")
    testpage.enter_description("testdesc")
    testpage.click_save_btn()
    time.sleep(2)
    assert testpage.get_res_text() == 'testtitle'

def test_step_4(browser):
    logging.info("Test4 starting")
    testpage = OperationsHelper(browser)
    testpage.click_contact_link()
    time.sleep(2)
    testpage.enter_contact_name("testname")
    testpage.enter_contact_mail("test@test.ru")
    testpage.enter_contact_content("testcontactcontent")
    time.sleep(2)
    testpage.click_contact_send_btn()
    time.sleep(3)
    assert testpage.get_alert() == 'Form successfully submitted'
