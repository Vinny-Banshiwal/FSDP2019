import pandas as pd
from selenium import webdriver
url="https://bidplus.gem.gov.in/bidlists"
driver = webdriver.Chrome("C:/Users/Honey/Downloads/chromedriver.exe")
driver.get(url)
a=[]
for i in range(1,11):
    bid=driver.find_element_by_class_name('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]')
    item=driver.find_element_by_class_name('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/strong')
    quantity==driver.find_element_by_class_name('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/strong')
a.append(bid.text)
