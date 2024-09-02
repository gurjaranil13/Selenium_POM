import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
driver.maximize_window() # Maximize the window
print(driver.current_url) # Show current url
print(driver.title) # Show page title
time.sleep(3) # for 3 seconds delay to see the execution
driver.close() # Close the current browser window