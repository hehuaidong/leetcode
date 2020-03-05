from selenium import webdriver
from lxml import etree
import json
import codecs
import codecs
# chromedriver的绝对路径
from selenium.common.exceptions import NoSuchElementException

driver_path = r'/usr/local/Caskroom/chromedriver/80.0.3987.16/chromedriver'

# 初始化一个driver，并且指定chromedriver的路径
driver = webdriver.Chrome(executable_path=driver_path)
# 请求网页
driver.get("https://leetcode-cn.com/problemset/algorithms/")

elements = driver.find_elements_by_xpath("//td/div/a")
print(elements)
for i in range(len(elements)):
    state = elements[i].get_attribute("class")
    hrefs = elements[i].get_property("href")
    if state == "":
        print(i)
        print(hrefs)
    elif state == "question-disabled":
        continue
    else:
        continue
