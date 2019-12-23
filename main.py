#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Michael Liao'
import time
import os
from selenium import webdriver  # 从selenium库导入webdirver
from selenium.webdriver.chrome.options import Options

os.environ["DISPLAY"]=":99"

url = 'http://192.168.62.1:8091/example/spectrogram/index.html?a=12333'
# Phantomjs
def test():
    brower = webdriver.PhantomJS(service_args=['--ssl-protocol=any'])  # 使用 webdirver.PhantomJS()方法新建一个phantomjs的对象，这里会使用到phantomjs.exe，环境变量path中找不到phantomjs.exe，则会报错

    brower.get('http://localhost:8091/example/spectrogram/index.html?a=123')  # 使用get()方法，打开指定页面。注意这里是phantomjs是无界面的，所以不会有任何页面显示
    time.sleep(40)
    brower.maximize_window()  # 设置phantomjs浏览器全屏显示
    time.sleep(2)
    brower.save_screenshot('lalala.png')  # 使用save_screenshot将浏览器正文部分截图，即使正文本分无法一页显示完全，save_screenshot 也可以完全截图

    brower.close()

def ChromeDriverNOBrowser():

   binary_location = '/usr/bin/google-chrome'
   chrome_driver_binary = '/usr/local/src/python-snapshot/drivers/chromedriver'

   chrome_options = Options()
   chrome_options.binary_location = binary_location
   chrome_options.add_argument('--headless')
   chrome_options.add_argument('--no-sandbox')
   chrome_options.add_argument('--disable-gpu')
   # chrome_options.add_argument('--user-data-dir="/usr/local/src"')
   chrome_options.add_argument('--disable-features=VizDisplayCompositor')
   chrome_options.add_argument('--disable-software-rasterizer')
   chrome_options.add_argument('--disable-dev-shm-usage')
   chrome_options.add_argument('blink-settings=imagesEnabled=false')

   chromedriver = chrome_driver_binary
   os.environ["webdriver.chrome.driver"] = chromedriver

   driverChrome = webdriver.Chrome(executable_path=chrome_driver_binary, options=chrome_options,  service_args=["--verbose", "--log-path=./cronJobChromeDriver.log"])
   driverChrome.get(url)
   time.sleep(10)
   driverChrome.maximize_window()
   time.sleep(2)
   screen_size = driverChrome.get_window_size()
   print(screen_size)
   driverChrome.save_screenshot('lalala.png')

   driverChrome.close()

if __name__=='__main__':
    ChromeDriverNOBrowser()
    # test()