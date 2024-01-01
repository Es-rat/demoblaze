import time
from selenium.webdriver.common.by import By


def signup(driver, url):
    time.sleep(3)
# signing up
    try:
        driver.find_element(By.LINK_TEXT, 'Sign up').click()
        time.sleep(3)
        driver.find_element(By.ID, 'sign-username').send_keys("Your Name")
        time.sleep(3)
        driver.find_element(By.ID, 'sign-password').send_keys("Yourpassword")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()
        time.sleep(3)
        AlertWindow = driver.switch_to.alert
        AlertWindow.accept()
        time.sleep(5)
        print('Sign Up is working: Successful ✔')
    except Exception as e:
        print('Sign Up is not working properly: Failed!')
        print(f"Error: {e}")

# Not Signing up
    try:
        driver.find_element(By.LINK_TEXT, 'Sign up').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[1]').click()
        time.sleep(3)
        print('Sign Up close is working: Successful ✔')
    except Exception as e:
        print('Sign Up close is not working properly: Failed!')
        print(f"Error: {e}")

