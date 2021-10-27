from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('[REDACTED FORM LINK]')

time.sleep(1)

# Fill out short answer questions.
shortAnswers = driver.find_elements(By.CSS_SELECTOR, 'input.quantumWizTextinputPaperinputInput')
shortAnswers[0].send_keys('Demeng#0001')
shortAnswers[1].send_keys('https://github.com/Demeng7215/AutoForm')
shortAnswers[2].send_keys('something')

# Select option 1 multiple choice question.
multipleChoices = driver.find_elements(By.CSS_SELECTOR, 'div.docssharedWizToggleLabeledLabelWrapper')
multipleChoices[0].click()

# Check options 2 and 3 for checkbox question.
checkboxes = driver.find_elements(By.CSS_SELECTOR, 'div.quantumWizTogglePapercheckboxInnerBox')
checkboxes[1].click()
checkboxes[2].click()

# Open the dropdown menu.
driver.find_element(By.CSS_SELECTOR, 'div.quantumWizMenuPaperselectEl').click()
time.sleep(1)

# Click the third option in the dropdown.
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[2]/div[5]').click()

time.sleep(2)

# Submit the form.
driver.find_element(By.XPATH, '//*[text()=\'Submit\']').click()
time.sleep(5)

driver.close()
