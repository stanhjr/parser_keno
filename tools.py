from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def parser_one_page(driver):

    time.sleep(2)
    reviews = driver.find_elements(By.CLASS_NAME, 'new-accordion.new-accordion--result')
    count = 0
    page_list = []

    for div_ in reviews:
        count += 1
        row_list = []
        driver.execute_script("arguments[0].scrollIntoView(true);", div_)

        label = div_.find_element_by_class_name("new-accordion__text").text
        row_list.append(label)
        list_ball = div_.find_elements(By.CLASS_NAME, 'new-ball__number')
        for ball in list_ball:
            row_list.append(ball.text)
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
            row_list.append(ball.text)
        page_list.append(row_list)
    return page_list


def refresh_page(driver):
    # review = driver.find_elements(By.CLASS_NAME, 'new-accordion.new-accordion--result')
    action = ActionChains
    action.send_keys(Keys.PAGE_UP)
    driver.execute_script("window.scrollTo(0, 500)")
