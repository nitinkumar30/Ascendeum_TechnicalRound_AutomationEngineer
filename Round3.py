# The assignment is to calculate the time it takes for the webpage to fully load, starting from the moment the
# “Mathup” webpage is opened to the moment the “Start’ button pops up.
# • The candidates have to repeat this process for ten times and then provide us with the average time it takes for the
# entire webpage to load.


import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

URL = "https://mathup.com/"
startXpath = "//div[text()='Start']"
total_time = []

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
    start_time = time.time()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, startXpath))
    )

    end_time = time.time()
    time_diff = end_time - start_time
    total_time.append(time_diff)

    print(f"Total time taken for round {i+1} is {time_diff:.2f}.")

average_time = sum(total_time)/len(total_time)
print(f"Average time taken is ==> {average_time:.2f}")
driver.quit()
