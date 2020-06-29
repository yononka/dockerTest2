import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
  driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
  driver.implicitly_wait(10)
  yield driver
  driver.quit()