import time

import requests
from selenium.webdriver.common.by import By


def alllinks1(driver, url):
    time.sleep(3)


def is_valid_link(links):
    try:
        response = requests.head(links)
        return response.status_code < 400
    except requests.exceptions.RequestException:
        return False
    links = [a.get_attribute("href") for a in driver.find_elements(By.TAG_NAME, 'a')]
    valid_links = []
    broken_links = []

    for link in links:
        if link:
            if is_valid_link(link):
                valid_links.append(link)
            else:
                broken_links.append(link)

    # Open the file in append mode
    file = open("output.txt", "a")

    file.write(f"Valid Links {len(valid_links)}- \n")
    print("Valid Links:")
    for link in valid_links:
        print(link)
        file.write(f"{link}\n")

    file.write(f"Broken Links {len(broken_links)}- \n")
    print("Broken Links:")
    for link in broken_links:
        print(link)
        file.write(f"{link}\n")
    file.close()
