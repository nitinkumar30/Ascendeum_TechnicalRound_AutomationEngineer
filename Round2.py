# The task is to open the Mathup website, click the "Start" button and record the difficulty level of the game in the
# terminal. This process should be repeated for ten times from opening of the “Mathup” website, hitting the "Start"
# button and noting the difficulty level for each time.
import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import tempfile

URL = "https://mathup.com/games/crossbit?mode=championship"
startXpath = "//div[text()='Start']"
difficultyLvl = "//div[text()='Difficulty']/ancestor::div[@class='GamePostStart_info__Rwi7G']//div[@class='GamePostStart_value__zH0b9']"

chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()
options = [
    "--window-size=1200,1200",
    "--ignore-certificate-errors"
    "--disable-gpu",
    "--no-sandbox",
    "--disable-dev-shm-usage",
    '--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

# Use a temporary directory as user data dir
temp_profile = tempfile.mkdtemp()
options.add_argument(f"--user-data-dir={temp_profile}")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

start_time = time.time()

for i in range(10):
    driver.get(URL)

    start_button = wait.until(EC.element_to_be_clickable((By.XPATH, startXpath)))
    start_button.click()

    difficulty_element = wait.until(EC.visibility_of_element_located((By.XPATH, difficultyLvl)))
    difficulty_level = difficulty_element.text

    print(f"Difficulty level for round {i+1} is {difficulty_level}.")


end_time = time.time()
print(f"Total time taken to complete this test is {(end_time - start_time):.2f}secs.")
driver.quit()
