"""
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
s = time.time()
while True:
    e = time.time()
    if (e-s > 1):
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        s = e
        print('c')
    
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://nebezb.com/floppybird/")
s = time.time()
while True:
    e = time.time()
    if (e-s > 0.5):
        webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()
        s = e
        print('s')
