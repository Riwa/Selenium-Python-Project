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
driver.find_element(By.XPATH,"//button[contains(text(),'Alert')]").click()
time.sleep(3)
#Récupérer l'alerte à l'aide d'une variable et switcher vers l'alerte
alertWindow = driver.switch_to.alert
print(alertWindow.text)
#ou bien textAlert = alertWindow.text
#accept(ok) comme ci on a cliqué sur le boution ok de l'alerte,dismiss = cancel
alertWindow.accept()

time.sleep(5)
#driver.close(fermer la 1ére page du navigateur),driver.quit(fermer toutes les fenêtres du navigateur exécuté par le script)
driver.quit()