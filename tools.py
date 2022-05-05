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
        row_list = []
        count += 1
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
                continue
        if len(row_list) == 21:
            page_list.append(row_list)
        if count == 20:
            break

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
                continue
        if len(row_list) == 21:
            page_list.append(row_list)

    return page_list


def calendar_step(driver, wait):
    wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="historyDate"]/div'))).click()
    time.sleep(1)

    date_list = driver.find_elements(By.CLASS_NAME, 'calendar-date')
    date_list = list(filter(lambda x: x.is_displayed(), date_list))

    date_selected = driver.find_element(By.CLASS_NAME, "calendar-date.calendar-date-selected")

    date_out_of_calendar_list = driver.find_elements(By.CLASS_NAME, "calendar-date-out.calendar-date")

    date_out_of_calendar_list = list(filter(lambda x: x.is_displayed(), date_out_of_calendar_list))

    date_list_result = []
    for elem in date_list:
        if elem not in date_out_of_calendar_list:
            date_list_result.append(elem)

    for pick in date_list_result:

        if int(date_selected.text) == 1:
            month_step(driver, wait)
            click_last_date_on_month(driver)
            break

        if int(date_selected.text) - int(pick.text) == 1:
            pick.click()
            break


def month_step(driver, wait):
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'calendar-month-select'))).click()
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'calendar-months')))
    calendar_months = driver.find_element(By.CLASS_NAME, 'calendar-months')
    month_list = calendar_months.find_elements(By.CLASS_NAME, 'calendar-date')
    time.sleep(0.5)

    month_now = calendar_months.find_element(By.CLASS_NAME, 'calendar-date.calendar-date-selected').text

    for month in month_list:
        if month_now == 'май' and month.text == "апр.":
            month.click()
            break
        if month_now == 'апр.' and month.text == "март":
            month.click()
            break
        if month_now == 'март' and month.text == "февр.":
            month.click()
            break


def click_last_date_on_month(driver):
    time.sleep(0.5)
    list_date_elements = driver.find_elements(By.CLASS_NAME, 'calendar-date')
    list_date_elements = list(filter(lambda x: x.is_displayed(), list_date_elements))

    date_out_of_calendar_list = driver.find_elements(By.CLASS_NAME, "calendar-date-out.calendar-date")
    date_out_of_calendar_list = list(filter(lambda x: x.is_displayed(), date_out_of_calendar_list))

    date_list_result = []
    for elem in list_date_elements:
        if elem not in date_out_of_calendar_list:
            date_list_result.append(elem)

    list_date = list(map(lambda x: x.text, date_list_result))
    list_date = list(filter(None, list_date))
    last_date = str(max(list(map(lambda x: int(x), list_date))))

    for date in date_list_result:
        if date.text == last_date:
            date.click()
            break
