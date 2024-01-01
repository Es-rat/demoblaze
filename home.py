import time
from selenium.webdriver.common.by import By


def home1(driver, url):
    time.sleep(3)

    # slide
    try:
        driver.find_element(By.CLASS_NAME, 'carousel-control-next-icon').click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, 'carousel-control-prev-icon').click()
        time.sleep(3)
        print('Slide: Successful ✔')
    except Exception as e:
        print('slide is not working: Failed!')
        print(f"Error: {e}")

        # Different function access
    try:
        driver.find_element(By.LINK_TEXT, 'Contact').click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, 'close').click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, 'About us').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="videoModal"]/div/div/div[1]/button').click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, 'Cart').click()
        time.sleep(2)
        driver.back()
        driver.find_element(By.ID, 'login2').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[1]/button/span').click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, 'Sign up').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[1]/button/span').click()
        time.sleep(2)
        # Categories
        driver.find_element(By.LINK_TEXT, 'Phones').click()
        time.sleep(10)
        driver.find_element(By.LINK_TEXT, 'Laptops').click()
        time.sleep(10)
        driver.find_element(By.LINK_TEXT, 'Monitors').click()
        time.sleep(10)
        print('All functions are working: Successful ✔')
    except Exception as e:
        print('All functions are not working properly: Failed!')
        print(f"Error: {e}")

    # Previous/Next
    try:
        driver.find_element(By.ID, 'next2').click()
        time.sleep(2)
        driver.find_element(By.ID, 'prev2').click()
        time.sleep(2)
        print('Previous and Next button working: Successful ✔')
    except Exception as e:
        print('Previous and Next buttons are not working properly: Failed!')
        print(f"Error: {e}")
