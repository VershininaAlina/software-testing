from selenium import webdriver
import time 

link = "http://localhost/litecart/admin/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[1]/td[2]/span/input')
    input1.send_keys("admin")
    input2 = browser.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[2]/td[2]/span/input')
    input2.send_keys("admin")
    button = browser.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла






