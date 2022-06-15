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
driver.find_element(By.XPATH,"(//button)[2]").click()
#Récupérer l'alerte à l'aide d'une variable et switcher vers l'alerte
time.sleep(3)
confirmWindow = driver.switch_to.alert
print(confirmWindow.text)
#ou bien textAlert = alertWindow.text
#On clique sur ANnuler c'est à dire on utilise dismiss() = cancel
confirmWindow.dismiss()
time.sleep(5)
#driver.close(fermer la 1ére page du navigateur),driver.quit(fermer toutes les fenêtres du navigateur exécuté par le script)
driver.quit()