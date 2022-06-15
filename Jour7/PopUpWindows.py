import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
#driver.get("https://the-internet.herokuapp.com/basic_auth"),(ds la popUp affioché on a besoin de mettre d
# l'user name ds le 1er élément et le pwd ds le 2éme élement mais on ne peut pas les distingué
#donc pr décontourner on va envoyer l'userName et le pwd ds l'url c'est à dire on va les concaténer comme suit
# admin:admin@juste après les //)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(1)
driver.quit()