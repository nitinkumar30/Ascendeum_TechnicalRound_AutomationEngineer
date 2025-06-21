# The task is to open the Mathup website, click the "Start" button and record the difficulty level of the game in the
# terminal. This process should be repeated for ten times from opening of the “Mathup” website, hitting the "Start"
# button and noting the difficulty level for each time.
import time
import chromedriver_autoinstaller

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://mathup.com/games/crossbit?mode=championship"
startXpath = "//div[text()='Start']"
difficultyLvl = "//div[text()='Difficulty']/ancestor::div[@class='GamePostStart_info__Rwi7G']//div[@class='GamePostStart_value__zH0b9']"

# driver = webdriver.Chrome()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

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

driver = webdriver.Chrome(options=chrome_options)


for i in range(10):
    driver.get(URL)
    time.sleep(5)
    driver.find_element(By.XPATH, startXpath).click()
    time.sleep(5)
    element = driver.find_element(By.XPATH, difficultyLvl)
    difficulty_level = element.text

    print(f"Difficulty level for round {i} is {difficulty_level}.")


driver.quit()
