import time

from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://duckduckgo.com')
browser.save_screenshot('1.png')

time.sleep(5)

browser.get('https://google.com')
browser.save_screenshot('2.png')
browser.refresh()

browser.quit()
