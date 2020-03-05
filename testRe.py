from lxml import etree
from selenium import webdriver

driver_path = r'/usr/local/Caskroom/chromedriver/80.0.3987.16/chromedriver'

# 初始化一个driver，并且指定chromedriver的路径
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://leetcode-cn.com/problems/symmetric-tree/description/")
element = driver.find_element_by_tag_name("h4")
# 获取题目描述
title = element.text
print(title)
elementLevel = driver.find_elements_by_tag_name("span")
levelText = elementLevel[3].text
print(levelText)
elementDescription = driver.find_elements_by_class_name("notranslate")[1]
description = elementDescription.get_attribute("innerHTML")
print(description)

codeElement = driver.find_element_by_class_name("view-lines")
code = codeElement.text
print(code)



