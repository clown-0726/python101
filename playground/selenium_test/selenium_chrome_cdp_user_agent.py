from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import time

options = ChromeOptions()
driver = Chrome(ChromeDriverManager().install(), options=options)

driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": "Fake User Agent"})

driver.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")

time.sleep(10)
driver.quit()

if __name__ == '__main__':
    pass
