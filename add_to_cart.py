import time
from selenium.webdriver.common.by import By


def add_cart(driver, url):
    time.sleep(3)
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
        driver.back()
        driver.back()
        driver.find_element(By.LINK_TEXT, 'Laptops').click()
        time.sleep(10)
        driver.find_element(By.LINK_TEXT, 'MacBook Pro').click()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, 'Add to cart').click()
        time.sleep(5)
        AlertWindow = driver.switch_to.alert
        AlertWindow.accept()
        time.sleep(3)
        driver.back()
        driver.back()
        driver.find_element(By.LINK_TEXT, 'Monitors').click()
        time.sleep(10)
        driver.find_element(By.LINK_TEXT, 'Apple monitor 24').click()
        time.sleep(5)
        driver.find_element(By.LINK_TEXT, 'Add to cart').click()
        time.sleep(5)
        AlertWindow = driver.switch_to.alert
        AlertWindow.accept()
        time.sleep(3)
        driver.back()
        driver.back()
        print('Product added: Successful ✔')
    except Exception as e:
        print('Product adding is not working properly: Failed!')
        print(f"Error: {e}")
# cart
    try:
        driver.find_element(By.LINK_TEXT, 'Cart').click()
        time.sleep(10)
        driver.find_element(By.LINK_TEXT, 'Delete').click()
        time.sleep(10)
        print('Cart Funtion(Delete): Successful ✔')
    except Exception as e:
        print('Cart function is not working properly: Failed!')
        print(f"Error: {e}")


