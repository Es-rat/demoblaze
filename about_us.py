import time
from selenium.webdriver.common.by import By


def abus(driver, url):
    time.sleep(3)

# About us
    try:
        driver.find_element(By.LINK_TEXT, 'About us').click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, 'vjs-big-play-button').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="videoModal"]/div/div/div[1]/button').click()
        time.sleep(2)
        print('video playing: Successful ✔')
    except Exception as e:
        print('Video is not playing properly: Failed!')
        print(f"Error: {e}")

# Close
    try:
        driver.find_element(By.LINK_TEXT, 'About us').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="videoModal"]/div/div/div[3]/button').click()
        time.sleep(2)
        print('Close Button: Successful ✔')
    except Exception as e:
        print('Close Button is not working properly: Failed!')
        print(f"Error: {e}")


