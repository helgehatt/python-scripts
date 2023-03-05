from time import sleep

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.set_preference("browser.download.dir", "~/Documents/Hehatt/")
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
options.set_preference("browser.helperApps.alwaysAsk.force", False)

driver = webdriver.Firefox(options=options)
driver.get("https://investor.vps.no/vit/sts?selskap")

driver.find_element(By.LINK_TEXT, "Brukernavn og passord").click()

username, password = driver.find_elements(By.TAG_NAME, "input")

username.send_keys(input("Enter username: "))
password.send_keys(input("Enter password: "))

# Click login
driver.find_elements(By.TAG_NAME, "button")[0].click()

# Select VPS account
driver.find_element(By.CSS_SELECTOR, ".btn-group button").click()

# Click mailbox (different buttons for desktop and mobile)
for element in driver.find_elements(By.CSS_SELECTOR, ".mailbox-link"):
    try:
        element.click()
    except exceptions.ElementNotInteractableException:
        pass

rows = driver.find_elements(By.CSS_SELECTOR, ".investorMessages tbody")[::-1]
rowiter = iter(rows)

for row in rowiter:
    row.find_element(By.TAG_NAME, "a").click()
    sleep(0.5)


# Navigate to next page
driver.find_elements(By.CSS_SELECTOR, ".pagination a")[-2].click()
