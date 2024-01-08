from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
driver = Chrome(ChromeDriverManager().install(), options=options)

# iPhone 11 Pro dimensions
set_device_metrics_override = dict({
    "width": 375,
    "height": 812,
    "deviceScaleFactor": 50,
    "mobile": True
})

driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', set_device_metrics_override)

driver.get("https://www.selenium.dev/")

time.sleep(10)
driver.quit()

if __name__ == '__main__':
    pass
