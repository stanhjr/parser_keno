from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from tools import parser_one_page, refresh_page

driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.maximize_window()

driver.get("https://tvbet.tv/demo/")

if __name__ == '__main__':
    wait = WebDriverWait(driver, 10)
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, "cookie-bar__close.js-close-cookie-bar"))).click()
    switch = wait.until(ec.frame_to_be_available_and_switch_to_it(driver.find_element(By.ID, "tvbet-iframe")))

    wait.until(ec.presence_of_element_located((By.ID, "menu_results"))).click()
    wait.until(ec.presence_of_element_located((By.ID, "historyGameFilter"))).click()

    time.sleep(1)
    wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="historyGameFilter"]/div[3]/div/div/div/div[17]'))).click()
    keno_btn = driver.find_element(By.ID, "tvbet-header")

    try:
        for i in range(2, 9):

            result = parser_one_page(driver)
            print(len(result))
            for list_ in result:
                print(list_)
            print('-----------------------------------------------------------------------------------------------------------------')

            driver.find_element(By.ID, f'pagerButton_{i}').click()

            driver.execute_script("arguments[0].scrollIntoView(true);", keno_btn)
            time.sleep(3)

    finally:
        driver.close()
