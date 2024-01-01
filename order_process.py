import time
from selenium.webdriver.common.by import By


def order(driver, url):
    time.sleep(3)

# login
    try:
        driver.find_element(By.ID, 'login2').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
        time.sleep(10)
        print('Log In is working: Successful ✔')
    except Exception as e:
        print('Log In is not working properly: Failed!')
        print(f"Error: {e}")

# Selecting products from home
    try:
        driver.find_element(By.LINK_TEXT, 'Nexus 6').click()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, 'Add to cart').click()
        time.sleep(5)
        AlertWindow = driver.switch_to.alert
        AlertWindow.accept()
        time.sleep(3)
        driver.back()
        driver.back()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, 'Sony vaio i5').click()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, 'Add to cart').click()
        time.sleep(3)
        AlertWindow = driver.switch_to.alert
        AlertWindow.accept()
        time.sleep(3)
        driver.back()
        driver.back()
        driver.find_element(By.LINK_TEXT, 'Phones').click()
        time.sleep(10)
        driver.find_element(By.LINK_TEXT, 'Iphone 6 32gb').click()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, 'Add to cart').click()
        time.sleep(5)
        AlertWindow = driver.switch_to.alert
        AlertWindow.accept()
        time.sleep(3)
        print('Product added: Successful ✔')
    except Exception as e:
        print('Product adding is not working properly: Failed!')
        print(f"Error: {e}")

# Place Order Close

    try:
        driver.find_element(By.LINK_TEXT, 'Cart').click()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button').click()
        time.sleep(10)
        driver.find_element(By.ID, 'name').send_keys("Ishraat")
        time.sleep(10)
        driver.find_element(By.ID, 'country').send_keys("Bangladesh")
        time.sleep(10)
        driver.find_element(By.ID, 'city').send_keys("Dhaka")
        time.sleep(10)
        driver.find_element(By.ID, 'card').send_keys("0000")
        time.sleep(10)
        driver.find_element(By.ID, 'month').send_keys("December")
        time.sleep(10)
        driver.find_element(By.ID, 'year').send_keys("2023")
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[1]').click()
        time.sleep(5)
        print('Place Order close: Successful ✔')
    except Exception as e:
        print('Place Order close function is not working properly: Failed!')
        print(f"Error: {e}")

# Place Order
    try:
        driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button').click()
        time.sleep(10)
        driver.find_element(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '/html/body/div[10]/div[7]/div/button').click()
        time.sleep(5)
        print('Place Order: Successful ✔')
    except Exception as e:
        print('Place Order function is not working properly: Failed!')
        print(f"Error: {e}")

    # logout
    try:
        driver.find_element(By.ID, 'logout2').click()
        time.sleep(2)
        print('Log out is working: Successful ✔')
    except Exception as e:
        print('Log  Out is not working properly: Failed!')
        print(f"Error: {e}")


