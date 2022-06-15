# Test case
# 1 lancer le navigateur
# 2 accéder à l'adresse https://www.saucedemo.com/
# 3 Saisir le username
# 4 Saisir le password
# 5 cliquer sur le bouton login
# 6 Ajouter le 1er article en cliquant sur le bouton ADD TO CART
# 7 Cliquer sur le panier
# 8 Vider le panier
# 9 Cliquer sur le bouton Checkout

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1 Lancer le navigateur
driver = webdriver.Chrome()
driver.maximize_window()
# 2 Accéder à l'adresse https://www.saucedemo.com/
driver.get("https://www.saucedemo.com/")
# 3 Saisir le username, en utilisant le localisateur ID
driver.find_element(By.ID, "user-name").send_keys("standard_user")
# 4 Saisir le password,, en utilisant le localisateur NAME
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
# 5 cliquer sur le bouton login, en utilisant le localisateur CLASS_NAME
driver.find_element(By.CLASS_NAME,"submit-button").submit()
# 6 Ajouter le 1er article en cliquant sur le bouton ADD TO, en utilisant le localisateur ID
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
# 7 Cliquer sur le panier,, en utilisant le localisateur CLASS_NAME
driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()
# 8 Vider le panier,, en utilisant le localisateur ID
driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
# 9 Cliquer sur le bouton Checkout,en utilisant le localisateur XPATH Absolu
driver.find_element(By.XPATH, "//button[@class='btn btn_action btn_medium checkout_button']").click()
#Temporiser pour voir Résultat
time.sleep(5)
driver.close()

