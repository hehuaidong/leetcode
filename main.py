from selenium import webdriver

import json
from pypinyin import pinyin, lazy_pinyin
# chromedriver的绝对路径
from selenium.common.exceptions import NoSuchElementException

driver_path = r'/Users/hehuaidong/pythonSpace/chromedriver'

# 初始化一个driver，并且指定chromedriver的路径
driver = webdriver.Chrome(executable_path=driver_path)
# 请求网页
driver.get("https://leetcode-cn.com/problemset/algorithms/")
urls = []
solutionsUrl = []
num = 1
# 通过page_source获取网页源代码
# print(driver.page_source)
# 获取题目列表数据
#题目 url对应关系list
problemDetailMap = {}

while True:
    elements = driver.find_elements_by_xpath("//td/div/a")
    for i in range(len(elements)):
        state = elements[i].get_attribute("class")
        hrefs = elements[i].get_property("href")
        title = elements[i].text
        if state == "":
            # 获取urls
            print(hrefs)
            problemDetailMap["hrefs"] = hrefs
            problemDetailMap["title"] = title
            solutionUrl = hrefs + "/solution/" + ("-".join(lazy_pinyin(title.lower())))+"-by-leetcode/";
            problemDetailMap["solutionUrl"] = solutionsUrl
            solutionsUrl.append(solutionUrl)
            urls.append(hrefs)
        elif state == "question-disabled":
            continue
        else:
            continue
        filename = "/Users/hehuaidong/pythonSpace/leetcode-spider/relationTable/" + "aa.json"
        f = open(filename, "a+", encoding="utf-8")
        f.write(json.dumps(problemDetailMap, ensure_ascii=False)+"\n")
        f.flush()
        f.close()

    # 2、模拟点击翻页按钮
    try:
        nextPageBtnElement = driver.find_element_by_class_name("reactable-next-page")
        nextPageBtnElement.click()
        num = num+1
    except NoSuchElementException:
        break

print(urls)
print("题目数为"+str(len(urls)))

# 处理 测试样例
for i in range(len(solutionsUrl)):
    driver.get(solutionsUrl[i])
    elementLi = driver.find_elements_by_tag_name("label")
    elementCode = driver.find_elements_by_tag_name("pre")
    source = []
    for j in range(len(elementLi)):

        maps = {}
        lang = elementLi[j].text
        print(lang)
        maps["lang"] = lang
        if j >= 1:
            elementLi[j].click()
        code = elementCode[j].text
        print(code)
        maps["code"] = code
        source.append(maps)

    print(source)

    data = {"url": urls[i], "source": source}
    filename = "/Users/hehuaidong/pythonSpace/leetcode-spider/sourceCode/sourceCode.json"
    f = open(filename, "a+", encoding="utf-8")
    f.write(json.dumps(data, ensure_ascii=False) + "\n")
    f.flush()
    f.close()
# 获取题目描述和提示代码
# for i in range(len(urls)):
#     detailMap = {}
#     # 完整url
#     driver.get(urls[i])
#     elementTitle = driver.find_element_by_tag_name("h4")
#     # 获取题目描述
#     title = elementTitle.text
#     print(title)
#     detailMap["title"]= title
#     filename = "./problenFile/"+str(title)+".json"
#     f = open(filename,  "a+", encoding="utf-8")
#     elementLevel = driver.find_elements_by_tag_name("span")
#     levelText = elementLevel[3].text
#     print(levelText)
#     detailMap["level"] = levelText
#     elementDescription = driver.find_elements_by_class_name("notranslate")[1]
#     description = elementDescription.get_attribute("innerHTML")
#     print(description)
#     detailMap["description"] = description
#     codeElement = driver.find_element_by_class_name("view-lines")
#     code = codeElement.text
#     print(code)
#     detailMap["code"] = code
#
#     f.write(json.dumps(detailMap, ensure_ascii=False))
#     f.flush()
#     f.close()


# 获取官方题解对应的源代码

