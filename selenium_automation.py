#Hi,

#!/usr/bin/python2.7
# -------------------------------------------------------------------------------
# Name:        script.py
# Purpose:     Web Scrapping through Selenium
#
# Author:      Hari K Misra
#
# Created:     29/5/2018
# -------------------------------------------------------------------------------

"""
1.Install latest Firefox (mine is 50.1.0)
	apt-get install firefox

2- Download latest geckodriver from this repo
	https://github.com/mozilla/geckodriver/releases

3- unzip the downloaded file
	tar -xvf geckodriver-v0.13.0-linux64.tar.gz
4- mv ./geckodriver /usr/bin

"""

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
import os
import sys


from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()
assert opts.headless


class Action(object):

    def selenium_automation(self, site_url):

        display = Display(visible=0, size=(800, 800))
        display.start()     
        try:
            print('-----------------------------------------------')
            print("Creating Browser Connection...")
            driver = webdriver.Firefox(options=opts)
            print("Driver connection successfull !!!")
            print("Getting driver details...")
            driver.get(site_url)
            driver.implicitly_wait(20)
            print("Wait driver completed !!!")
            page = driver.page_source
            print("Scraping with Beautiful Soap...")
            soup = BeautifulSoup(page.encode("UTF-8"), "html.parser")
            print("Web Scrapping Completed !!!")
            return soup
        except Exception as err:
            print("Exception occurred to get the site details")
            driver.close()
            sys.exit()
        finally:
            driver.close()

obj = Action()
site_url = raw_input("Enter the website to Scrap:")
scrapped_data = obj.selenium_automation(site_url)
#print "Web site scrape data:", scrapped_data
with open("output.txt", 'w') as f:
	f.write(str(scrapped_data))


"""
1. What is web scrapping?
2. why it is used?
3. What is the benefit of selenium+python
4. How to run web driver in headless mode
5. What is Beautiful soup?
6. 
"""