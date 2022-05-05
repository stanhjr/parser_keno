from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from models.db_api import db_api
from tools import parser_one_page, calendar_step

driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.maximize_window()
driver.get("https://tvbet.tv/demo/")
wait = WebDriverWait(driver, 10)

if __name__ == '__main__':
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, "cookie-bar__close.js-close-cookie-bar"))).click()
    switch = wait.until(ec.frame_to_be_available_and_switch_to_it(driver.find_element(By.ID, "tvbet-iframe")))

    wait.until(ec.presence_of_element_located((By.ID, "menu_results"))).click()
    wait.until(ec.presence_of_element_located((By.ID, "historyGameFilter"))).click()

    time.sleep(1)
    wait.until(
        ec.presence_of_element_located((By.XPATH, '//*[@id="historyGameFilter"]/div[3]/div/div/div/div[17]'))).click()

    try:
        for step in range(3):
            keno_btn = driver.find_element(By.ID, "tvbet-header")
            calendar_step(driver, wait)
            for i in range(2, 11):
                page_list = parser_one_page(driver)
                db_api.set_raw(page_list)
                try:
                    driver.find_element(By.ID, f'pagerButton_{i}').click()
                except:
                    continue
                driver.execute_script("arguments[0].scrollIntoView(true);", keno_btn)
                time.sleep(2)
    finally:
        db_api.render_excel_file()
        driver.close()
