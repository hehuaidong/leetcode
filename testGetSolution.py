
from selenium import webdriver

url = "https://leetcode-cn.com/problems/smallest-range-i/solution/zui-xiao-chai-zhi-i-by-leetcode/"


driver_path = r'/usr/local/Caskroom/chromedriver/80.0.3987.16/chromedriver'

# 初始化一个driver，并且指定chromedriver的路径
driver = webdriver.Chrome(executable_path=driver_path)
# 请求网页
driver.get(url)
elementLi = driver.find_elements_by_tag_name("label")
elementCode = driver.find_elements_by_tag_name("pre")
source = []
for i in range(len(elementCode)):

    maps = {}
    lang = elementLi[i].text
    print(lang)
    maps["lang"] = lang
    if i >= 1:
        elementLi[i].click()
    code = elementCode[i].text
    print(code)
    maps["code"] = code
    source.append(maps)

print(source)
