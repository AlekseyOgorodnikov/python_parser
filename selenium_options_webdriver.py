import time
from selenium import webdriver

# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# disable webdriver mode

# # for older ChromeDriver under version 79.0.3945.16
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

# for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

# work in background
options.headless = True

driver = webdriver.Chrome(options=options)

driver.get("https://mynickname.com/generate")

while True:
    button_xpath = "/html/body/div[1]/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input"
    driver.find_element_by_xpath(button_xpath).click()

    link = driver.find_element_by_id('register').get_attribute('href')[36:]
    print(f'Nickname: {link}')
