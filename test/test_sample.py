from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import allure


@allure.feature('Feature1')
@allure.story('Story1')
@allure.step('step1')
def test_title(browser):
    browser.get("http://www.google.com")
    title = "Google"
    print("first test")
    # screenshot = browser.save_screenshot('test.png')
    assert title == browser.title

@allure.feature('Feature2')
@allure.story('Story2')
@allure.step('step2')
def test_search(browser):
    browser.get("http://www.google.com")
    browser.find_element_by_name('q').send_keys('wikipedia')
    browser.find_element_by_name('btnK').click()
    title = 'Поискк'
    print("second test")
    # screenshot = browser.save_screenshot('test.png')
    # WebDriverWait(browser, 10).until(
    #     EC.title_contains(title))
    assert title in browser.title

def test_just_assert():
    assert 2==2