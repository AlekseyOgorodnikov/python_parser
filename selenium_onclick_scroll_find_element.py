import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://youtube.com')

# Скролинг страницы
html = browser.find_element_by_tag_name('html')

for i in range(50):
    html.send_keys(Keys.DOWN)

# Обработка событий типа клик и ввод данных в форму отправки или регистрации
# xpath_button = '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/tp-yt-paper-button'
# button = browser.find_element_by_xpath(xpath_button).click()
#
# form_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
# browser.find_element_by_xpath(form_xpath).send_keys('example')


# Получение элементов при помощи selenium
# block = browser.find_element_by_class_name('style-scope ytd-rich-grid-renderer')
# all_video = block.find_elements_by_tag_name('ytd-rich-item-renderer')
#
# for video in all_video:
#     print(video.get_attribute('class'))
