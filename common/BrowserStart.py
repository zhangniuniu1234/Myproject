from common.ReadConfig  import getBrowserinfo
import os
from  selenium import webdriver
from  common.CapPic import CapPic
from common.LogGen import LogGen

logger=LogGen(logger="浏览器启动加载").getLog()

def BrowserStart():
    browsername = getBrowserinfo('BrowserName')
    url = getBrowserinfo('Url')
    # print(browsername)
    # 判断浏览器的类型，浏览器的分解
    if (browsername == 'Chrome'):
        driver = webdriver.Chrome()
        logger.info("启动浏览器")
        driver.get(url)
        logger.info("打开测试网页")
        CapPic(driver)

    if (browsername == 'Firefox'):
        driver = webdriver.Firefox()
        driver.get(url)

BrowserStart()



