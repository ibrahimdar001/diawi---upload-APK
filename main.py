from setup import tear_up,tear_down
from upload import file_upload
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

try:
    driver = tear_up()
    upload_file = 'C:\\Users\\M Ibrahim Dar\\Downloads\\com.afwsamples.testdpc_9.0.1-9001_minAPI21(nodpi)_apkmirror.com.apk'
    driver.find_element(By.ID,'uploader_browse').click()

    file_upload()
    driver.find_element(By.XPATH, "//div[@class='upload-send']/input").click()

    upload_status = (By.XPATH,"//div[@class='upload-result']/div/span")
    upload_result = WebDriverWait(driver,100).until(EC.presence_of_element_located(upload_status))
    image_source = driver.find_element(By.XPATH, "//div[@class='barcode']/img").get_attribute("src")
    
    response = requests.get(image_source)
    with open(f"{upload_result.text}.png","wb") as out_file:
        out_file.write(response.content)

finally:
    tear_down()    




