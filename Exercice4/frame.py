import time

from selenium import webdriver
#Lancer le navigateur
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
#Accéder à l'url https://www.google.ca/
driver.get("http://demo.automationtesting.in/Frames.html")
#cliquer sur le lien single frame
driver.find_element(By.LINK_TEXT,"Single Iframe").click()
#Entrer dans le  frame SingleFrame
driver.switch_to.frame("SingleFrame")
#localiser le champs de saisie et écrire Arwa
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Arwa")
time.sleep(2)
#sortir du  frame SingleFrame et retourner à la page principale
driver.switch_to.default_content()
#cliquer sur le lien Iframe with in an Iframe
driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()
#Entrer dans le 1er frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']"))
#Entrer dans le 2éme frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@src='SingleFrame.html']"))
#localiser le champs de saisie et écrire Hello
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Hello")
time.sleep(2)
#Sortir du 2éme frame et aller au 1er frame(frame parent)
driver.switch_to.parent_frame()
#sortir du  1er frame  et retourner à la page principale
driver.switch_to.default_content()

time.sleep(2)
driver.quit()

