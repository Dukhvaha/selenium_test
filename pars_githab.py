from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация браузера
driver = webdriver.Chrome()

def connect_to_codewars():
    try:
        driver.get('https://github.com/login')
        time.sleep(5)
        user_name = driver.find_element(by=By.XPATH, value='//*[@id="login_field"]')
        user_name.send_keys('Dukhvaha')
        time.sleep(3)
        password = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
        password.send_keys('dukvaha_95')
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='//*[@id="login"]/div[4]/form/div/input[13]').click()
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[5]/div/div/aside/div/div/loading-context/div/div[1]/div/div[1]/a').click()
        time.sleep(3)
        repasitori_name = driver.find_element(by=By.XPATH, value='//*[@id=":r5:"]')
        repasitori_name.send_keys('selenium_test')
        time.sleep(3)
        opisany = driver.find_element(by=By.XPATH, value='//*[@id=":ra:"]')
        opisany.send_keys('Простой тест selenium регистрация в Github')
        time.sleep(3)
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[5]/main/react-app/div/form/div[5]/button/span/span').click()
        time.sleep(10)

    except Exception as error:
        print(f'Ощибка {error}')

connect_to_codewars()