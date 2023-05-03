from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import urllib
import urllib.request

def artikul_selenium_func(url_func):
    url = url_func # ССЫЛКА НА ТОВАР НА WB

    service = Service(executable_path='C:/chromedriver/chromedriver')  # УКАЗЫВАЕМ ПУТЬ ДО ДРАЙВЕРА
    browser = webdriver.Chrome(service=service)

    try:
        browser.get(url)
        time.sleep(2)
        src = browser.find_element_by_xpath("//div[@class='mix-block__photo-zoom photo-zoom j-wba-card-item']/div[@class='photo-zoom__img-plug img-plug']/div[@class='zoom-image-container']/img").get_attribute("src")
        urllib.request.urlretrieve(src, "filename.png") # НАЗВАНИЕ ФАЙЛА
        browser.quit()
        
    except Exception as ex:
        print(ex)
        browser.quit()

    browser.quit()