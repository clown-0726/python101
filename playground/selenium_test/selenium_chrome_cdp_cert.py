from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
driver = Chrome(ChromeDriverManager().install(), options=options)

driver.execute_cdp_cmd("Security.enable", {})
driver.execute_cdp_cmd("Security.setIgnoreCertificateErrors", {"ignore": True})

driver.get("https://expired.badssl.com/")

time.sleep(10)
driver.quit()

if __name__ == '__main__':
    pass
