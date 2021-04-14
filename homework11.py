from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

link = "http://localhost/litecart/en/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element_by_xpath('//*[@id="box-account-login"]/div/form/table/tbody/tr[5]/td/a')
    a.click()
    list = Select(browser.find_element_by_tag_name("select"))
    list.select_by_visible_text("United States")
    input1 = browser.find_element_by_xpath('//*[@id="create-account"]/div/form/table/tbody/tr[2]/td[1]/input')
    input1.send_keys("Alina")
    input2 = browser.find_element_by_xpath('//*[@id="create-account"]/div/form/table/tbody/tr[2]/td[2]/input')
    input2.send_keys("Vershinina")
    input3 = browser.find_element_by_xpath('//*[@id="create-account"]/div/form/table/tbody/tr[3]/td[1]/input')
    input3.send_keys("test")
    input4 = browser.find_element_by_xpath('//*[@id="create-account"]/div/form/table/tbody/tr[4]/td[1]/input')
    input4.send_keys("76666")
    input5 = browser.find_element_by_xpath('//*[@id="create-account"]/div/form/table/tbody/tr[4]/td[2]/input')
    input5.send_keys("tokio")
    input6 = browser.find_element_by_xpath('//*[@id="create-account"]/div/form/table/tbody/tr[6]/td[1]/input')
    input6.send_keys("a12345vershinina@dnomads.pro")
    input9 = browser.find_element_by_xpath('//*[@id="create-account"]/div/form/table/tbody/tr[6]/td[2]/input')
    input9.send_keys("89138558802")
    input8 = browser.find_element_by_xpath('//*[@id="create-account"]/div/form/table/tbody/tr[8]/td[2]/input')
    input8.send_keys("Superpass123!")
    input7 = browser.find_element_by_xpath('//*[@id="create-account"]/div/form/table/tbody/tr[8]/td[1]/input')
    input7.send_keys("Superpass123!")
    
  
    
    f = browser.find_element_by_xpath('//*[@id="create-account"]/div/form/table/tbody/tr[9]/td/button')
    f.click()
    out = browser.find_element_by_xpath('//*[@id="box-account"]/div/ul/li[4]/a')
    out.click()
    input10 = browser.find_element_by_xpath('//*[@id="box-account-login"]/div/form/table/tbody/tr[1]/td/input')
    input10.send_keys("a12345vershinina@dnomads.pro")
    input20 = browser.find_element_by_xpath('//*[@id="box-account-login"]/div/form/table/tbody/tr[2]/td/input')
    input20.send_keys("Superpass123!")
    button = browser.find_element_by_xpath('//*[@id="box-account-login"]/div/form/table/tbody/tr[4]/td/span/button[1]')
    button.click()
    out2 = browser.find_element_by_xpath('//*[@id="box-account"]/div/ul/li[4]/a')
    out2.click()


finally:
    time.sleep(10)
    browser.quit()

# не забываем оставить пустую строку в конце файла 


