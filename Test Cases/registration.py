
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open Chrome and navigate to invu.ge
driver = webdriver.Chrome()
driver.get("https://invu.ge")
try:
	wait = WebDriverWait(driver, 10)
	# 2. Click the registration button
	button = wait.until(
		EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'რეგისტრაცია')]"))
	)
	button.click()
	# 3. Enter first name
	input_field = wait.until(
		EC.presence_of_element_located((By.XPATH, "(//input[@id='firstName'])[1]"))
	)
	input_field.send_keys("Gigaa")
	# 4. Enter last name
	last_name_field = wait.until(
		EC.presence_of_element_located((By.XPATH, "(//input[@id='lastName'])[1]"))
	)
	last_name_field.send_keys("Khintibidzee")
	# 5. Enter email
	email_field = wait.until(
		EC.presence_of_element_located((By.XPATH, "(//input[@id='email'])[1]"))
	)
	email_field.send_keys("gigakhintibidze16@gmail.com")
	# 6. Enter password
	password_field = wait.until(
		EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
	)
	password_field.send_keys("giga123")
	# 7. Enter confirm password
	confirm_password_field = wait.until(
		EC.presence_of_element_located((By.XPATH, "//input[@id='confirmPassword']"))
	)
	confirm_password_field.send_keys("giga123")
	# 8. Click 'Create Account' button
	create_account_button = wait.until(
		EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create Account']"))
	)
	create_account_button.click()
	time.sleep(5)  # Keep browser open for 5 seconds after click
finally:
	driver.quit()
