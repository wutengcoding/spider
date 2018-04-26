from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'd:\applications\chromedriver.exe')
driver.get("https://www.toutiao.com/a6540567317728723470/")
# 执行js得到整个页面内容
html = driver.execute_script("return document.documentElement.outerHTML")
print(html)
print ("Headless Chrome Initialized")

driver.quit()