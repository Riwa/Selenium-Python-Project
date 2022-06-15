#Lancer le navigateur
#Accéder à l'url https://www.google.ca/
#Lancer une recherche avec le mot Selenium dans la zone de recherche
#Choisir Selenium webdriver parmis la liste d'autosuggestion
import time

from selenium import webdriver
#Lancer le navigateur
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
#Accéder à l'url https://www.google.ca/
driver.get("https://www.google.ca/")
#Lancer une recherche avec le mot Selenium dans la zone de recherche
driver.find_element(By.XPATH,"//input[@class='gLFyf gsfi']").send_keys("Selenium")
#Choisir Selenium webdriver parmis la liste d'autosuggestion
#search_results = driver.find_elements(By.XPATH, "//div[@class='UUbT9']/div//ul/li")
search_results = driver.find_elements(By.XPATH, "//ul[@role='listbox']//li/descendant::div/span")
#//ul[@role='listbox']//li/descendant::div/span
print(len(search_results))
for element in search_results:
    print(element.text)
    #Si "selenium webdriver" existe ds le text de resultats
    if "selenium webdriver" in element.text:

        element.click()
        time.sleep(4)
        break

time.sleep(4)
driver.close()


