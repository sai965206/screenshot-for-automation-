from selenium import webdriver
from selenium.webdriver.common.by import By
from screenshot import *

option = webdriver.EdgeOptions()
option.add_experimental_option("detach",True)
driver = webdriver.Edge(options=option)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("iphone")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
element = driver.find_element(By.XPATH,"//*[@class='tUxRFH']")
obj = saving(x=int(element.rect["x"]//1),y=int(element.rect["y"]//1),width=element.rect["width"],height=element.rect["height"]+80)
obj.capture()
driver.close()
