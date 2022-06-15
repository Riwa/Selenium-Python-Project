import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
#Mettre le driver 1ére fenetre ds une variable
parentWindowId = driver.current_window_handle
#L'identifiant de la 1ere fenêtre : CDwindow-8E8C9BC1EC89C569831F136EE84D5317
print(parentWindowId)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
#Récup un seul id de fenêtre
#driver.current_window_handle
#Récup la liste des ids de fenêtres ouvertes
windowsHandelsIds = driver.window_handles
#1ere fenêtre
parentWindowId = windowsHandelsIds[0]
#2éme fenêtre
childWindowId = windowsHandelsIds[1]
#les ids générés sont dynamiques
print("parentWindowId:" ,parentWindowId)
print("childWindowId:" ,childWindowId)
#Basculer vers la 2éme fenêtre, récup url et titre (2éme fenêtre)
driver.switch_to.window(childWindowId)
url2 = driver.current_url
title2 = driver.title
print(url2)
print(title2)
driver.switch_to.window(parentWindowId)
print("#################################################################")
url1 = driver.current_url
title1 = driver.title
print(url1)
print(title1)

#2éme approche: parcourrir la liste de windowsHandleIds et vrf le titre
for winId in windowsHandelsIds:
    driver.switch_to.window(winId)
    if driver.title == title1:
        driver.close()


time.sleep(4)
driver.quit()
