from selenium import webdriver
import time 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

link = "http://localhost/litecart/admin/"

browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[1]/td[2]/span/input')
input1.send_keys("admin")
input2 = browser.find_element_by_xpath('//*[@id="box-login"]/form/div[1]/table/tbody/tr[2]/td[2]/span/input')
input2.send_keys("admin")
button = browser.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button')
button.click()


def is_element_present(driver, *args):
  try:
    driver.find_element(*args)
    return True
  except NoSuchElementException:
    return False

status_OK=True

try:
  items = browser.find_elements_by_id("app-")
  total_items_count = len(items)
  count = 0

  while count < total_items_count:
    time.sleep(1)
    items[count].click()
    if not is_element_present(browser, By.TAG_NAME, "h1"):
        status_OK = False
        break

    sub_items = browser.find_elements_by_css_selector("li[id*=doc]")
    total_sub_items_count = len(sub_items)
    count2 = 0
    while  count2 < total_sub_items_count:
        time.sleep(1)
        sub_items[count2].click()
        if not is_element_present(browser, By.TAG_NAME, "h1"):
            status_OK = False
            break
        sub_items = browser.find_elements_by_css_selector("li[id*=doc]")
        count2 = count2 + 1

    items = browser.find_elements_by_id("app-")
    count = count + 1



finally:
    if status_OK:
        print("All checks are green!")
    else:
        print("Something went wrong!")
    browser.quit()


# не забываем оставить пустую строку в конце файла
 