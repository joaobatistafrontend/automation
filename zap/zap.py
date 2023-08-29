from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

drive = webdriver.Chrome()
drive.get('https://web.whatsapp.com/')
time.sleep(30)

contato = ['test']