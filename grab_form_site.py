from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome()
driver.get('https://scrapeme.live/shop/')
sleep(1)
try:
    out_put = driver.find_elements(By.TAG_NAME, 'h2')
    for out in out_put:
        found = out.find_element(By.TAG_NAME, 'h2')
except NoSuchElementException:
    print("there is No Element To Print ... ")
input()