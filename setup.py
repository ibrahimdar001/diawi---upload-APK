from selenium import webdriver

driver = webdriver.Chrome()

def tear_up():    
    driver.get("https://www.diawi.com/")
    driver.maximize_window()

    driver.implicitly_wait(10)
    return driver

def tear_down():
    driver.close()
    driver.quit()