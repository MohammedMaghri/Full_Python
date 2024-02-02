from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

def function_open_path(path, message):
    search_bar = driver.find_element(By.XPATH, path)
    try:
        search_bar.send_keys(Keys.ENTER)
    except NoSuchElementException:
        print("No available...?")
    for char in message:
        search_bar.send_keys(char)
    search_bar.send_keys(Keys.ENTER)
    sleep(2)
search_for = input("Please Enter the Song U wanna Play ... ?")
driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')
sleep(1)
function_open_path("//input[@id='search']", search_for)
sleep(5)
videos = driver.find_elements(By.XPATH, "//ytd-video-renderer[@class='style-scope ytd-item-section-renderer']")
index = 1
for video in videos:
    title_element = video.find_element(By.XPATH, ".//a[@id='video-title']")
    print([index], title_element.get_attribute("title"))
    print("\n")
    if index == 3:
        break
input ()
driver.quit()
