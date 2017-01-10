# encoding:utf-8
import bs4
from selenium import webdriver
import time
from datetime import datetime

def tbspider():
    print datetime.now()
    driver = webdriver.PhantomJS(executable_path="phantomjs.exe")
    driver.get("http://item.jd.com/2200381.html")
    time.sleep(7)
    print driver.page_source
    driver.get_screenshot_as_file("33.jpg")
    print datetime.now()
    driver.close()
if True:
    tbspider()