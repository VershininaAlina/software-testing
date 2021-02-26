from selenium import webdriver
import time 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

link = "http://localhost/litecart/admin/"

browser = webdriver.Chrome()
browser.get(link)
    
def is_element_present(driver, By.CssSelector(#box-apps-menu)):
  try:
    driver.find_element(By.CssSelector(#content > h1 > font))
    return True
  except NoSuchElementException:
    return False

  finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла
 