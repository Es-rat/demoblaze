import time

from rich.theme import Theme
from rich.console import Console
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from home import home1
from contact import cont
from about_us import abus
from add_to_cart import add_cart
from sign_up import signup
from login import login1
from order_process import order
from all_links import alllinks1

chromeOptions = Options()
custom_theme = Theme({'success': 'green', 'error': 'bold red'})
serv_obj = Service("C:/BrowserDrivers/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
console = Console(theme=custom_theme)
driver.get("https://www.demoblaze.com/")
driver.maximize_window()

# home
try:
    home1(driver, "https://www.demoblaze.com/")
    console.print('Home: Successful ✔', style='success')
except Exception as e:
    console.print('Home: Failed! 👎', style='error')
    console.print(f"Error from Home: {e}")
    time.sleep(10)
# Contact
try:
    cont(driver, "https://www.demoblaze.com/")
    console.print('Contact: Successful ✔', style='success')
except Exception as e:
    console.print('Contact: Failed! 👎', style='error')
    console.print(f"Error from Contact: {e}")
    time.sleep(10)
# # about us
try:
    abus(driver, "https://www.demoblaze.com/")
    console.print('About: Successful ✔', style='success')
except Exception as e:
    console.print('About Us: Failed! 👎', style='error')
    console.print(f"Error from About us: {e}")

# # Add To Cart
try:
    add_cart(driver, "https://www.demoblaze.com/cart.html")
    console.print('Add to Cart: Successful ✔', style='success')
except Exception as e:
    console.print('Add to Cart: Failed! 👎', style='error')
    console.print(f"Error from Add to Cart: {e}")

# sign up
try:
    signup(driver, "https://www.demoblaze.com/")
    console.print('Sign Up: Successful ✔', style='success')
except Exception as e:
    console.print('Sign Up: Failed! 👎', style='error')
    console.print(f"Error from Add to Sign Up: {e}")

# #log in
try:
    login1(driver, "https://www.demoblaze.com/")
    console.print('Log In-Log Out: Successful ✔', style='success')
except Exception as e:
    console.print('Log In-Log Out: Failed! 👎', style='error')
    console.print(f"Error from Add to Log In-Log Out: {e}")

# Order Process
try:
    order(driver, "https://www.demoblaze.com/")
    console.print('Order Process: Successful ✔', style='success')
except Exception as e:
    console.print('Order Process: Failed! 👎', style='error')
    console.print(f"Error from Add to Order Process: {e}")

# all links
try:
    alllinks1(driver, "https://www.demoblaze.com/")
    console.print('All Links: Successful ✔', style='success')
except Exception as e:
    console.print('All Links: Failed! 👎', style='error')
    console.print(f"Error from Add to All Links: {e}")

driver.close()
