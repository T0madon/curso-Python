from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )
    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )
    return chrome_browser

if __name__ == '__main__':
    TIME_TO_WAIT = 10
    #Example
    options = ()
    browser = make_chrome_browser(*options)

    browser.get('https://www.google.com')

    #Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )

    search_input.send_keys('Hello World')
    search_input.send_keys(Keys.ENTER)

    results = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.ID, 'search')
        )
    )

    # results = browser.find_element(By.ID, 'search')

    print(results)
    
    print('Falha')
    # links = results.find_elements(By.TAG_NAME, 'a')
    # print(links[0])


    time.sleep(TIME_TO_WAIT)