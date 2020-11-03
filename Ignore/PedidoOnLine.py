from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sqlite3


try:
    # Path para linux
    #/home/linuxlite/Documents/PYTHON/WSP/
    driver = webdriver.Firefox(executable_path=r"/home/linuxlite/Documents/PYTHON/WSP/geckodriver")
except:
    # Path para windows
    driver = webdriver.Chrome(executable_path=r"D:\Programación\Python\Archivos\Driver Chrome para Selenium\chromedriver_win32\chromedriver.exe")

driver.get("https://web.whatsapp.com/")