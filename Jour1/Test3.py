#Test Case
#------------------
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
# 2) Naviguer vers l'url https://opensource-demo.orangehrmlive.com/
# 3) Entrer username (Admin)
# 4) Entrer password (admin123)
# 5) Cliquer sur le bouton Login
# 6) recuperer le titre de la page(titre actuel)
# 7) Verifier le titre de la page: OrangeHRM  (attendu)
# 8) Fermer le navigateur
import time

from selenium.webdriver.chrome.service import  Service
from selenium import webdriver
from selenium.webdriver.common.by import By

#service_obj = Service("C:\\Users\\Owner\\Desktop\\Driver\\chromedriver.exe")  # spécifier l'emplacement de driver
# 1) Ouvrir le navigateur(chrome/firefox/Edge)
#driver = webdriver.Chrome(service=service_obj)    # créer le driver webDriver Chrome
# 2) Naviguer vers l'url https://opensource-demo.orangehrmlive.com/
driver = webdriver.Chrome() # on n'a pas besoin de mettre l'emplacement car on a glissé le chemin de driver ds le script de Python
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()  # ouvrir le driver chrome en plein écran
# 3) Entrer username (Admin)
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
# 4) Entrer password (admin123)
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
# 5) Cliquer sur le bouton Login
driver.find_element(By.ID, "btnLogin").click()
# 6) recuperer le titre de la page(titre actuel)
act_title =  driver.title  # recupére le titre de la page
# 7) Verifier le titre de la page: OrangeHRM  (attendu)
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("Le test Login  est passed")
else:
    print("Le test Login  est failed")
time.sleep(4)   # Temporisateur (synchronisation)
# 8) Fermer le navigateur
driver.close()





