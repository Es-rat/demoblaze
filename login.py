import time
from selenium.webdriver.common.by import By


def login1(driver, url):
    time.sleep(3)

# login
    try:
        driver.find_element(By.ID, 'login2').click()
        time.sleep(2)
        driver.find_element(By.ID, 'loginusername').send_keys("Ishraat Zahaan")
        time.sleep(3)
        driver.find_element(By.ID, 'loginpassword').send_keys("Password")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
        time.sleep(10)
        print('Log In is working: Successful ✔')
    except Exception as e:
        print('Log In is not working properly: Failed!')
        print(f"Error: {e}")
# logout
    try:
        driver.find_element(By.ID, 'logout2').click()
        time.sleep(2)
        print('Log out is working: Successful ✔')
    except Exception as e:
        print('Log  Out is not working properly: Failed!')
        print(f"Error: {e}")
# close
    try:
        driver.find_element(By.ID, 'login2').click()
        time.sleep(2)
        driver.find_element(By.ID, 'loginusername').send_keys("Ishraat Zahaan")
        time.sleep(3)
        driver.find_element(By.ID, 'loginpassword').send_keys("Password")
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[1]').click()
        time.sleep(10)
        print('Log In close is working: Successful ✔')
    except Exception as e:
        print('Log In close is not working properly: Failed!')
        print(f"Error: {e}")
