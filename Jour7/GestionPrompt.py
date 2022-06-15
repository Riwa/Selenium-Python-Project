import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#les différents localisateurs:
#(//button)[1]
#//button[@onclick='jsAlert()']
#//button[text()='Click for JS Alert']
#//button[contains(text(),'Alert')]
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
time.sleep(3)
#Récupérer l'alerte à l'aide d'une variable et switcher vers l'alerte
alertWindows = driver.switch_to.alert
print(alertWindows)
alertWindows.send_keys('Hi Arwa')
time.sleep(3)
alertWindows.accept()
time.sleep(3)
driver.quit()