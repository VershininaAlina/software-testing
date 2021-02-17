from selenium import webdriver
import time 

link = "https://software-testing.ru"

try:
    browser = webdriver.Chrome()
    browser.get(link)
finally:
    browser.quit()


