#Lancer le navigateur
#Accéder à l'url https://www.google.ca/
#Lancer une recherche avec le mot Selenium dans la zone de recherche
#Récupérer la liste des suggestions
#Parcourir la liste des suggestions
#Choisir Selenium webdriver parmis la liste des suggestions
import time

from selenium import webdriver

#Lancer le navigateur
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
#Accéder à l'url https://www.google.ca/
driver.get("https://www.google.ca/")
#Lancer une recherche avec le mot Selenium dans la zone de recherche
driver.find_element(By.NAME,'q').send_keys("selenium")
#Choisir Selenium webdriver parmis la liste d'autosuggestion
drop_sug = driver.find_elements(By.XPATH,"//ul[@role='listbox']//li/descendant::div/span")
#Afficher la taille de la liste des suggestions
print(len("drop_sug"))

#Parcourir la liste des suggestions
for element in drop_sug:
    print(element.text)
# Si l'élement de la liste des susggestions est égale à "selenium webdriver", Cliquer dessus et sortir
    if element.text.__eq__('selenium webdriver'):
        element.click()
        break

time.sleep(2)
#Fermer le navigateur
driver.close()


