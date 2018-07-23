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
            target = '"Friend\'s Name"'

			# Replace the below string with your own message
			string = "Message sent using Python!!!"

			x_arg = '//span[contains(@title,' + target + ')]'
			group_title = wait.until(EC.presence_of_element_located((
				By.XPATH, x_arg)))
			group_title.click()
			inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
			input_box = wait.until(EC.presence_of_element_located((
				By.XPATH, inp_xpath)))
			for i in range(100):
				input_box.send_keys(string + Keys.ENTER)
				time.sleep(1)
            # page = driver.page_source
            # print("Scraping with Beautiful Soap...")
            # soup = BeautifulSoup(page.encode("UTF-8"), "html.parser")
            # print("Web Scrapping Completed !!!")
            # return soup
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