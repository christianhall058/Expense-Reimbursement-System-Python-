from selenium import webdriver
import time

from poms.login_page import LoginPage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5000/login")

lp = LoginPage(driver)
lp.enter_employee_credentials()
lp.click_login_button()

driver.quit()