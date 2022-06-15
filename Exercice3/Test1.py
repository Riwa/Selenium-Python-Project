#Lancer le navigateur
#Accéder à l'url http://omayo.blogspot.com/
#Faire une selection dans une liste à selection unique
#Faire une selection dans une liste multiselection
#Faire uen selectiondans une liste multiselection
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")

#Faire une selection dans une liste à selection unique
drop_newslettesrs = driver.find_element(By.ID,"drop1")
newslettesrs = Select(drop_newslettesrs)

# Selection par texte visible(dynamiq)
# newslettesrs.select_by_visible_text("doc 2")
# Selection par index(statique)
# newslettesrs.select_by_index(2)
newslettesrs.select_by_value("ghi")

#Faire une selection dans une liste multiselection
drop_multiselection_box = driver.find_element(By.ID,"multiselect1")
multiselection_box = Select(drop_multiselection_box)
# Selection par texte visible(dynamiq)
multiselection_box.select_by_visible_text("Volvo")
time.sleep(2)
multiselection_box.select_by_visible_text("Swift")
time.sleep(2)
multiselection_box.select_by_visible_text("Audi")
time.sleep(2)

multiselection_box.deselect_by_visible_text("Volvo")
time.sleep(4)
driver.close()
