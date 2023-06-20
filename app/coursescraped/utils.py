from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def get_driver():
    time.sleep(3)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")

    driver = webdriver.Remote(
        command_executor='http://headless_chrome:3000/webdriver',
        options=chrome_options,
    )
    return driver

def get_courses(driver):
    course_elements = driver.find_elements(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[@class="row"]/div[@class="column"]/ul')
    course_list = []
    for items in course_elements:
        try:
            item = items.find_element(By.XPATH, './/li/a').text
            course_name = item.replace('Cursos gratis ', '').replace('sobre ', '').replace('para la ', '').replace('de ', '')
            course_list.append(course_name)
        except NoSuchElementException:
            pass
    return course_list