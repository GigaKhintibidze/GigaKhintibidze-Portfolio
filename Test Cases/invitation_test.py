
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
	# 2. Click the login button
	login_button = wait.until(
		EC.element_to_be_clickable((By.XPATH, "//a[@class='desktop-login'][contains(text(),'შესვლა')]"))
	)
	login_button.click()
	# 3. Enter email
	email_field = wait.until(
		EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
	)
	email_field.send_keys("khintibidzegiga@gmail.com")
	# 4. Enter password
	password_field = wait.until(
		EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
	)
	password_field.send_keys("Giga123")
	# 5. Click 'Sign In' button
	sign_in_button = wait.until(
		EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign In']"))
	)
	sign_in_button.click()
	# 6. Click the specified flex items-center button
	flex_button = wait.until(
		EC.element_to_be_clickable((By.XPATH, "(//a[@class='flex items-center p-4 bg-gradient-to-r from-amber-600 to-orange-600 text-white rounded-lg hover:from-amber-700 hover:to-orange-700 transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl'])[1]"))
	)
	flex_button.click()
	# 7. Click the first template card
	first_template_card = wait.until(
		EC.element_to_be_clickable((By.XPATH, "(//div[@class='w-full h-full flex items-center justify-center p-2 sm:p-4'])[1]"))
	)
	first_template_card.click()
	# 8. Enter invitation name
	invitation_name = wait.until(
		EC.presence_of_element_located((By.XPATH, "(//input[@placeholder='მაგალითად, ემა და ნოას ქორწილი'])[1]"))
	)
	invitation_name.send_keys("ქორწილის მოსაწვევი")
	# 9. Enter date
	date_input = wait.until(
		EC.presence_of_element_located((By.XPATH, "(//input[@type='date'])[1]"))
	)
	date_input.send_keys("12/12/2025")
	# 10. Click 'მოსაწვევის შექმნა' button
	create_invitation_button = wait.until(
		EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(),'მოსაწვევის შექმნა')])[1]"))
	)
	create_invitation_button.click()
	time.sleep(5)  # Keep browser open for 5 seconds after last input
finally:
	driver.quit()






