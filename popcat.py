import time
from selenium import webdriver


browser = webdriver.Chrome("D:\google download\chromedriver_win32 (1)\chromedriver.exe")
browser.get("https://popcat.click/")

link = browser.find_element_by_xpath("/html/body/div[1]/div")
while True:
    link.click()
    time.sleep(0.55)
