#Lancer le navigateur
#Accéder à l'url https://www.google.ca/
#Lancer une recherche avec le mot Selenium dans la zone de recherche
#Choisir Selenium webdriver parmis la liste d'autosuggestion
import time

from selenium import webdriver
#Lancer le navigateur
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window();
# Ouvrir le lien google.ca
driver.get("https://www.google.ca/")
#Saisir le mot recherché Selenium
mot_recherche=driver.find_element(By.NAME, "q")
mot_recherche.send_keys("Selenium")
time.sleep(5)
#Récupérer la liste des suggestions
suggestions = driver.find_elements(By.XPATH, "//form[@action='/search' and @role='search']//ul[@role='listbox']//li//span")
print(len(suggestions))
#parcourir la liste des suggestions
#Faire un clique sur l'element de la liste si egale à "selenium webdriver"
for element in suggestions:
    print(element.text)
    if element.text.__eq__('selenium webdriver'):
        element.click()
        break
time.sleep(2)
driver.close()