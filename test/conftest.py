import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
# from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.add_argument('--headless')
    # driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    driver = webdriver.Chrome("../chromedriver", options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
