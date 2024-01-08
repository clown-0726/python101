from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
driver = Chrome(ChromeDriverManager().install(), options=options)

driver.execute_cdp_cmd("Network.enable", {})
driver.execute_cdp_cmd("Network.emulateNetworkConditions", {
    "offline": False,
    "latency": 100,
    "downloadThroughput": 20000,
    "uploadThroughput": 10000,
    "connectionType": "cellular3g",
})

driver.get("https://www.makemytrip.com/")

time.sleep(10)
driver.quit()

if __name__ == '__main__':
    pass
