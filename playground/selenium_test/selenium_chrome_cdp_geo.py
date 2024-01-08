from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
driver = Chrome(ChromeDriverManager().install(), options=options)

Map_coordinates = dict({
    "latitude": 41.8781,
    "longitude": -87.6298,
    "accuracy": 100
})
driver.execute_cdp_cmd("Emulation.setGeolocationOverride", Map_coordinates)

driver.get("https://my-location.org/")

time.sleep(10)
driver.quit()

if __name__ == '__main__':
    pass
