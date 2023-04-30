import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.skyscanner.net"  # Replace with the URL you want to scrape

options = webdriver.ChromeOptions()

options.add_argument('--disable-extensions')
options.add_argument('--headless')


driver = webdriver.Chrome(options=options)  # Replace with the path to your chromedriver executable

driver.get(url)
# bypass bot page

# Wait for the cookie dialog to appear and then click the "OK" button
try:
    accept_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'OK')]"))
    )
    accept_button.click()

    print("Cookie dialog dismissed")
except:
    print("No cookie dialog found")


print(driver.page_source)

print("Rendered HTML content saved to output.html")


driver.quit()  # Close the browser
