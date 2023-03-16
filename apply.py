from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

link = ""
MY_EMAIL = ""
MY_PASSWORD = ""

op = Options()
op.add_experimental_option("detach", True) # This doesn't close the browser when the program done
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=op)
driver.maximize_window()
driver.get(link)

try:
    sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
    sign_in_button.click()
except NoSuchElementException:
    pass

username_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
username_field.send_keys(MY_EMAIL)
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(MY_PASSWORD, Keys.ENTER)
