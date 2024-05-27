from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

BUERGERBUERO_WEBSITE = 'https://tempus-termine.com/termine/index.php?anlagennr=13&anlagentoken=Uq9dpZv7&anwendung=1&infotext=buergerbuero'
TIME_INTERVAL = 10 * 60 # 10 min

ANMELDUNG = 'Anmeldung-422-mittermin'
REISEPASS = 'Antrag_RP-416-mittermin'
CHOOSE_DATETIME = '//input[@value="Datum und Uhrzeit auswählen"]'
CHECKBOX = '//input[@type="checkbox"]'
CONFIRM = '//input[@id="confirm"]'
TERMIN_DATE = 'nav_menu2'

def select(driver, id, value):
  select_tag= driver.find_element(By.ID, id)
  selector = Select(select_tag)
  selector.select_by_value(value)

def click_button(driver, xpath):
  button = driver.find_element(By.XPATH, xpath)
  button.click()

def click_buttons(driver, xpath):
  buttons = driver.find_elements(By.XPATH, xpath)
  for button in buttons:
    button.click()

def find_text(driver, classname):
  return driver.find_element('class name', classname).text

def navigate(driver):
  select(driver, ANMELDUNG, "1")
  select(driver, REISEPASS, "1")

  driver.implicitly_wait(1)

  click_button(driver, CHOOSE_DATETIME)
  click_buttons(driver, CHECKBOX)
  click_button(driver, CONFIRM)

  earliest_date = find_text(driver, TERMIN_DATE)

  print (earliest_date)
  

while True:
  driver = webdriver.Chrome()
  driver.get(BUERGERBUERO_WEBSITE)
  
  navigate(driver)
  
  driver.quit()

  time.sleep(TIME_INTERVAL)
