from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def parser_one_page(driver):
    wait = WebDriverWait(driver, 10)
    time.sleep(3)
    reviews = driver.find_elements(By.CLASS_NAME, 'new-accordion.new-accordion--result')
    count = 0
    page_list = []

    for div_ in reviews:
        count += 1
        row_list = []
        driver.execute_script("arguments[0].scrollIntoView(true);", div_)

        label = div_.find_element_by_class_name("new-accordion__text").text
        row_list.append(label)
        time.sleep(1)

        wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, 'new-ball__number')))
        list_ball = div_.find_elements(By.CLASS_NAME, 'new-ball__number')
        for ball in list_ball:
            try:
                ball_text = ball.text
                row_list.append(ball_text)
            except StaleElementReferenceException:
                row_list.append('X')
        page_list.append(row_list)
        if count == 20:
            break

    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView(true);", reviews[20])

    time.sleep(2)

    review = driver.find_elements(By.CLASS_NAME, 'new-accordion.new-accordion--result')

    for div_ in review[20:]:
        driver.execute_script("arguments[0].scrollIntoView(true);", div_)
        row_list = []
        label = div_.find_element_by_class_name("new-accordion__text").text
        row_list.append(label)
        list_ball = div_.find_elements(By.CLASS_NAME, 'new-ball__number')
        for ball in list_ball:
            try:
                ball_text = ball.text
                row_list.append(ball_text)
            except StaleElementReferenceException:
                row_list.append('X')

    return page_list


def refresh_page(driver):
    # review = driver.find_elements(By.CLASS_NAME, 'new-accordion.new-accordion--result')
    action = ActionChains
    action.send_keys(Keys.PAGE_UP)
    driver.execute_script("window.scrollTo(0, 500)")


def search_date_elem(date_list: list, date_now: int):
    ...


def calendar_step(driver, wait):
    wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="historyDate"]/div'))).click()
    time.sleep(1)
    date_list = driver.find_elements(By.CLASS_NAME, 'calendar-date')

    date_selected = driver.find_element(By.CLASS_NAME, "calendar-date.calendar-date-selected")

    for pick in date_list:
        if int(date_selected.text) == 1:
            wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'calendar-month-select'))).click()
            mounth_list = driver.find_elements(By.CLASS_NAME, 'calendar-date')

            break
        if int(date_selected.text) - int(pick.text) == 1:
            pick.click()
            break