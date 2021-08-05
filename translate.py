from googletrans import Translator
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
chrome_driver = input('D:\\Desktop\\chromedriver.exe seklinde chromedriver.exe yolunu yaziniz')
driver = webdriver.Chrome(chrome_driver,options=options)

driver.get("https://www.bbc.com/news/science_and_environment")

first_news = driver.find_element_by_xpath('//*[@id="topos-component"]/div[4]/div/div[1]/div/div[1]/div/div[2]/div[1]/a')
first_news.click()

news = driver.find_element_by_xpath('//*[@id="main-content"]/div[5]/div/div[1]/article')
translator = Translator()

cumleler = news.text.split("\n")
driver.get("https://translate.google.com/?hl=tr&sl=en&tl=tr&op=translate")

for i in cumleler:
    if len(i)>30:
        english = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
        english.send_keys(Keys.CONTROL, "a")
        english.send_keys(i)
        time.sleep(5)
        turkish = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]/span/span')

        print(i)
        print(turkish.text)
        print()
    else:
        pass


