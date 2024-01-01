import time
from selenium.webdriver.common.by import By


def cont(driver, url):
    time.sleep(3)

    # send message
    try:
        driver.find_element(By.LINK_TEXT, 'Contact').click()
        time.sleep(3)
        driver.find_element(By.ID, 'recipient-email').send_keys('ishu@ishu.com')
        time.sleep(2)
        driver.find_element(By.ID, 'recipient-name').send_keys('Ishraat')
        time.sleep(2)
        driver.find_element(By.ID, 'message-text').send_keys('Very good website!')
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="exampleModal"]/div/div/div[3]/button[2]').click()
        time.sleep(2)
        AlertWindow = driver.switch_to.alert
        AlertWindow.accept()
        time.sleep(3)
        print('Sending Message: Successful ✔')
    except Exception as e:
        print('Send message is not working properly: Failed!')
        print(f"Error: {e}")


# close
    try:
        driver.find_element(By.LINK_TEXT, 'Contact').click()
        time.sleep(5)
        driver.find_element(By.ID, 'recipient-email').send_keys('ishu@ishu.com')
        time.sleep(2)
        driver.find_element(By.ID, 'recipient-name').send_keys('Ishraat')
        time.sleep(2)
        driver.find_element(By.ID, 'message-text').send_keys('Very good website!')
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="exampleModal"]/div/div/div[3]/button[1]').click()
        time.sleep(2)
        print('Close Button: Successful ✔')
    except Exception as e:
        print('Close Button is not working properly: Failed!')
        print(f"Error: {e}")

    # driver.close()
